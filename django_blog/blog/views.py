from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        # Optionally automatically log the user in
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/profile.html', context)