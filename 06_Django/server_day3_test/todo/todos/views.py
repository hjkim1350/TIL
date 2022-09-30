from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content_ = request.GET.get("content_")

    Todo.objects.create(content=content_)

    return redirect("todos:index")
    # return render(request, "todos/index.html")


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect("todos:index")
