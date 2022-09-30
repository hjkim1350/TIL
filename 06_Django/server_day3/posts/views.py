from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post

# Create your views here.


def index(request):
    #  모든 글 목록을 보여준다
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()

    # 2. template에 보내준다.
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def detail(request, pk_):
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def new(request):
    return render(request, "posts/new.html")


def edit(request, pk_):
    post = Post.objects.get(pk=pk_)
    context = {
        "post": post,
    }
    return render(request, "posts/edit.html", context)


def create(request):
    # DB에 저장
    # 1) parameter로 날아온 데이터를 받음
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2) DB에 저장
    Post.objects.create(title=title, content=content)

    # context = {
    #     "title": title,
    #     "content": content,
    # }

    #    return render(request, "posts/create.html", context)
    return redirect("posts:index")


def update(request, pk_):
    post = Post.objects.get(pk=pk_)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    post.title = title_
    post.content = content_

    post.save()

    return redirect("posts:detail", post.pk)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect("posts:index")
