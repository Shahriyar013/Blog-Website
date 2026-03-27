from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'data': data})

def signup(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('/login/')
    return render(request, 'signup.html')

def loginuser(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

@login_required
def create(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST['title'],
            text=request.POST['text'],
            user=request.user
        )
        return redirect('/')
    return render(request, 'create.html')

def detail(request, id):
    post = Post.objects.get(id=id)
    com = Comment.objects.filter(post=post)
    like = Like.objects.filter(post=post).count()
    return render(request, 'detail.html', {
        'post': post,
        'com': com,
        'like': like
    })

@login_required
def comment(request, id):
    if request.method == "POST":
        p = Post.objects.get(id=id)
        Comment.objects.create(
            post=p,
            user=request.user,
            text=request.POST['text']
        )
    return redirect(f'/post/{id}/')

@login_required
def like(request, id):
    p = Post.objects.get(id=id)
    l = Like.objects.filter(post=p, user=request.user)

    if l.exists():
        l.delete()
    else:
        Like.objects.create(post=p, user=request.user)

    return redirect(f'/post/{id}/')