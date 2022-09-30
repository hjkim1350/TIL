from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index),
    path("is-odd-even/<int:num>", views.is_odd_even),
    path("calculate/<int:num1>/<int:num2>", views.calculate),
    path("pastlife/", views.pastlife),
    path("pastlife_result/", views.pastlife_result),
    path("ko_lipsum/", views.ko_lipsum),
    path("ko_lipsum_result/", views.ko_lipsum_result),
]
