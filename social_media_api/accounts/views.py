from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, permissions
from rest_framework.generics import get_object_or_404


from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={'request': request}).data
        return Response({
            'user': data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user, context={'request': request}).data,
            'token': token.key
        })


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self):
        # return the current authenticated user
        return self.request.user
    

class FollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if request.user == target_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)


        request.user.follow(target_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


class UnfollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if request.user == target_user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)


        request.user.unfollow(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)


class FollowingListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        following_users = request.user.following.all()
        serializer = UserSerializer(following_users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowersListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        followers = request.user.followers.all()
        serializer = UserSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)