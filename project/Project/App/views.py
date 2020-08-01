from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.contrib import auth
from .models import MsUser, Post, Comment
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'registartion/login.html')
        
        auth.authenticate(
            request, 
            found_user,
            backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        if(len(found_user)>0):
            error = '해당 계정은 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create(
            username = request.POST['username'],
            password = request.POST['password']
        )

        MsUser.objects.create(
            user = new_user.username,
            name = request.POST['name'],
            kisoo = request.POST['kisoo'],
            email = request.POST['email'],
            major = request.POST['major'],
            idNumber = request.POST['idNumber']
        )

        auth.login(request,new_user)
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')

    return render (request, 'registration/signup.html')


@login_required(login_url = '/registration.login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.MsUser,
            category = request.POST['category']
        )
        return redirect('detail', new_post.pk)

    return render(request, 'board.html')

@login_required(login_url = '/registration.login')
def edit(request):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(

            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('board_detail', post_pk)
    
    return render(request, 'board_detail_edit.html', {'post':post })



def board(request):
    board_post = Post.objects.all()
    return render(request, 'board.html', {'board_posts' : board_posts})



def board_detail (request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Comment.objects.create (
            post = post,
            content = request.POST ['post'],
            author = request.user
        )
        return redirect('board_detail', post_pk)
    return render(request,'board_detail.html', {'post':post})