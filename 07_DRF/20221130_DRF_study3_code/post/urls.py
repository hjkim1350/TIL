from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list),
    path('create/', views.post_create),
    path('<int:pk>/', views.post_detail),
    path('update/<int:pk>/', views.post_update),
    path('delete/<int:pk>/', views.post_delete),
    path('comment/', views.comment_list),
    path('<int:post_pk>/comment/create/', views.comment_create),
    path('recomment/', views.recomment_list),
    path('<int:post_pk>/comment/<int:comment_pk>/recomment/create/', views.recomment_create),
]