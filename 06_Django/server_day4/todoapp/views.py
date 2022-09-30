from functools import total_ordering
from django.shortcuts import render, redirect
from .models import todoapp

# Create your views here.

# root 페이지
def index(request):
    #  모든 글 목록을 보여준다
    # 1. DB에서 모든 글을 불러온다.
    todos = todoapp.objects.order_by("id")
    total = todoapp.objects.all().count()

    # 2. template에 보내준다.
    context = {
        "todos": todos,
        "total": total,
    }

    return render(request, "todoapp/index.html", context)


# 할 일 추가 페이지
def create(request):
    # DB에 저장
    # 1) parameter로 전송된 데이터를 받음
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    # 2) DB 저장
    todoapp.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )
    return redirect("todoapp:index")


# 상태 변경 시 진행 상태 변경
def update(request, pk):
    todo = todoapp.objects.get(pk=pk)

    todo.completed = not todo.completed

    todo.save()

    return redirect("todoapp:index")


# 할 일 삭제
def delete(request, pk):
    # pk에 해당하는 글 삭제
    todoapp.objects.get(id=pk).delete()

    return redirect("todoapp:index")
