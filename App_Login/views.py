import os

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.context_processors import media

from App_Dashboard.forms import PostForm
from App_Dashboard.models import Post
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as lg
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile

# Create your views here.

def login(request):
    return redirect('App_Login:log-sign')

def log_sign(request):
    if request.method == 'POST' and 'signin' in request.POST:
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username1, password=password1)
        if user is not None:
            lg(request, user)
            return redirect('App_Dashboard:home')
    if request.method == 'POST' and 'signup' in request.POST:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        registered = True
        data_dict = {
            'user_id': user.id,
            'type': request.POST['type'],
        }
        UserProfile.objects.create(**data_dict)
        return HttpResponseRedirect(reverse('App_Login:log-sign'))

    return render(request, 'App_Login/log_sign.html', context={'title': 'Sign In/Sign Up'})

@login_required
def edit_profile(request):

    if request.user.is_superuser:
        messages.error(request, 'You are a superuser')
        return HttpResponseRedirect(reverse('App_Login:profile'))

    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)

        if request.FILES and request.POST.get('profile_pic-clear'):
            pass
        else:
            if request.FILES:
                if request.user.user_profile.profile_pic:
                    if os.path.exists(request.user.user_profile.profile_pic.path):
                        os.remove(request.user.user_profile.profile_pic.path)

            if request.POST.get('profile_pic-clear'):
                if request.user.user_profile.profile_pic:
                    if os.path.exists(request.user.user_profile.profile_pic.path):
                        os.remove(request.user.user_profile.profile_pic.path)

        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            messages.success(request, 'Profile Updated')
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/edit-profile.html', context={'title': 'Edit Profile', 'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:log-sign'))


@login_required
def profile(request):
    form = PostForm()
    diction = {
        'title': 'User List',
        'form': form
    }
    return render(request, 'App_Login/user.html', context=diction)

@login_required
def users(request):
    users = UserProfile.objects.filter(type=2)
    print(users)
    diction = {
        'title': 'User List',
        'users': users
    }
    return render(request, "App_Login/users.html", context=diction)