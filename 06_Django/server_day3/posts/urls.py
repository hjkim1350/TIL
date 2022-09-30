from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete"),
    # 요청 - 응답
    # 어떤 주소(detail/)로 요청하면
    # 어떤 VIEW(detail)로 응답할까?
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("edit/<int:pk_>", views.edit, name="edit"),
    path("update/<int:pk_>", views.update, name="update"),
]
