from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from App_Dashboard import forms
from App_Dashboard.forms import PostForm, ReplyFrom, DesignerMessageFrom
from App_Dashboard.models import DesignerInfo, Post, ContactUs, React, Reply, DesignerMessage
from App_Login.models import UserProfile


# @login_required
def home(request):
    # country_list = Country.objects.all()
    posts = Post.objects.all()
    customers_count = UserProfile.objects.filter(type=1)
    designers_count = UserProfile.objects.filter(type=2)
    designers = UserProfile.objects.filter(type=2)
    # aboutus = AboutUs.objects.all()
    diction = {
        'title': 'Dashboard',
        'customers_count': customers_count,
        'designers_count': designers_count,
        'designers': designers,
        'posts': posts
    }
    return render(request, "App_Dashboard/home.html", context=diction)


@login_required
def country(request):
    country_list = Country.objects.all()
    diction = {
        'title': 'Country_List',
        'country_list': country_list
    }
    return render(request, "App_Dashboard/country.html", context=diction)


@login_required
def country_form(request):
    form = forms.CountryForm()

    if request.method == 'POST':
        form = forms.CountryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Country Added Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'title': "Add Country",
        'country_form': form
    }
    return render(request, "App_Dashboard/country_form.html", context=diction)


@login_required
def edit_country(request, country_id):
    country_info = Country.objects.get(pk=country_id)
    form = forms.CountryForm(instance=country_info)

    if request.method == 'POST':
        form = forms.CountryForm(request.POST, instance=country_info)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Country Updated Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_country.html', context=diction)


@login_required
def delete_country(request, country_id):
    Country.objects.get(pk=country_id).delete()
    messages.success(request, 'Country Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Dashboard:country'))


@login_required
def designer_info(request):
    designers = DesignerInfo.objects.all()
    print(designers)
    diction = {
        'title': 'Designer Info',
        'designers': designers,
    }
    return render(request, "App_Dashboard/designers_list.html", context=diction)


@login_required
def add_designer(request):
    form = forms.DesignerInfoForm()

    if request.method == 'POST':
        form = forms.DesignerInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Designer Info Added Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))
    diction = {
        'title': "Add Designer Info",
        'designer_info_form': form
    }
    return render(request, "App_Dashboard/designers_form.html", context=diction)


@login_required
def view_designer(request, designer_id):
    designer = UserProfile.objects.get(pk=designer_id)
    posts = Post.objects.filter(author_id=designer.user.id)

    diction = {
        'title': 'Designer Details',
        'designer': designer,
        'posts': posts,
    }
    return render(request, 'App_Dashboard/view_designers.html', context=diction)\


@login_required
def edit_designer(request, designer_id):
    designer_info = DesignerInfo.objects.get(pk=designer_id)
    form = forms.DesignerInfoForm(instance=designer_info)

    if request.method == 'POST':
        form = forms.DesignerInfoForm(request.POST, request.FILES, instance=designer_info)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Designer Updated Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_designers.html', context=diction)


@login_required
def delete_designer(request, designer_id):
    DesignerInfo.objects.get(pk=designer_id).delete()
    messages.success(request, 'Designer Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))


@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Designer Post Added Successfully')
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {
        'title': "Profile Info",
    }
    return render(request, "App_Login/user.html", context=diction)


def view_posts(request):
    posts = Post.objects.all()
    reacts = React.objects.all()

    diction = {
        'title': 'Blog Post',
        'posts': posts,
        'reacts': reacts,

    }
    return render(request, 'App_Dashboard/view_posts.html', context=diction)

@login_required
def view_post(request, post_id):
    posts = Post.objects.all()
    post = Post.objects.get(pk=post_id)
    replies = Reply.objects.filter(post_id=post_id)
    reacts = React.objects.filter(post=post_id, user=request.user)
    total_reacts = React.objects.filter(post=post_id)

    diction = {
        'title': 'Post Details',
        'post': post,
        'replies': replies,
        'reacts': reacts,
        'total_reacts': total_reacts,
        'posts': posts
    }
    return render(request, 'App_Dashboard/view_post.html', context=diction)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Post Updated Successfully')
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_post.html', context=diction)


@login_required
def delete_post(request, post_id):
    Post.objects.get(pk=post_id).delete()
    messages.success(request, 'Post Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Login:profile'))


def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        data_dict = {
            'name': name,
            'email': email,
            'contact': contact,
            'message': message,
        }
        ContactUs.objects.create(**data_dict)
        messages.success(request, 'Message has been sent successfully ')
        return HttpResponseRedirect(reverse('App_Dashboard:home'))


def react_post(request, post_id):
    react = React.objects.filter(post=post_id, user=request.user)
    if react:
        react.delete()
        messages.error(request, 'You unlike the post successfully')
    else:
        data_dict = {
            'post': post_id,
            'user': request.user,
        }
        React.objects.create(**data_dict)
        messages.success(request, 'You like the post successfully')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def reply(request):
    if request.method == 'POST':
        data_dict = {
            'post_id': request.POST['post_id'],
            'user': request.user,
            'message': request.POST['message']
        }

        Reply.objects.create(**data_dict)
        messages.success(request, 'You comment replied successfully')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def desginerMessage(request):
    if request.method == 'POST':
        data_dict = {
            'designer_user': request.POST['designer_id'],
            'customer_user': request.user,
            'message': request.POST['message']
        }

        DesignerMessage.objects.create(**data_dict)
        messages.success(request, 'Messeage sent successfully')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def myMessageList(request):
    mymessages = DesignerMessage.objects.filter(designer_user=request.user.id)
    customerMessages = DesignerMessage.objects.filter(customer_user=request.user.id)
    users = User.objects.all()
    print(messages)
    diction = {
        'title': 'Messages',
        'mymessages': mymessages,
        'customerMessages': customerMessages,
        'users': users
    }
    return render(request, 'App_Dashboard/messages.html', context=diction)


def designerMessageReply(request, message_id):
    message = DesignerMessage.objects.get(pk=message_id)
    editReplyFrom = DesignerMessageFrom(instance=message)

    if request.method == 'POST':
        form = DesignerMessageFrom(request.POST, 'request.FILES', instance=message)
        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Message replied Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:myMessageList'))
    diction = {
        'editReplyFrom': editReplyFrom
    }

    return render(request, 'App_Dashboard/reply_message.html', context=diction)