from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data.get('email')
    if commit:
        user.save()
    return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)


class PostForm(forms.ModelForm):
    # user-facing tag input, comma-separated
    tags_field = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, python).",
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3', 'class': 'form-control'})
    )
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'rows': 10, 'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required.')
        return title
    
    def clean_tags_field(self):
        raw = (self.cleaned_data.get('tags_field') or '').strip()
        # optional: sanitize, remove duplicates, lower-case
        if not raw:
            return []
        tag_names = [t.strip() for t in raw.split(',') if t.strip()]
        # unique, keep order
        seen = set()
        result = []
        for t in tag_names:
            key = t.lower()
            if key not in seen:
                seen.add(key)
                result.append(t)
        return result
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a comment...',
                'class': 'form-control'
            })
        }

    def clean_content(self):
        content = (self.cleaned_data.get('content') or '').strip()
        if not content:
            raise forms.ValidationError('Comment cannot be empty.')
        return content