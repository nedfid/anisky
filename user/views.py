from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from user.forms import LoginForm, UpdateUserForm, UpdateProfileForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


def user_profile(request, username):
    user = User.objects.get(username=username)

    return render(request, 'user/user_profile.html', context={'u': user})


def user_all(request):
    users = User.objects.all()

    return render(request, 'user/user_all.html', context={'users': users})


def user_settings(request, username):
    if request.user.is_authenticated == True and request.user.username == username:
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                # messages.success(request, 'Your profile is updated successfully')
                return redirect(to='user_settings', username=username)
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

            return render(request, 'user/user_settings.html', context={'user_form': user_form, 'profile_form': profile_form})
    else:
        return redirect(f'/u/{username}/')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')