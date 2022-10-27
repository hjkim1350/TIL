from django.urls import path
from . import views
from django.conf import settings # 추가
from django.conf.urls.static import static # 추가

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('comments/<int:pk>', views.comments_create, name='comments_create'),
    path('comments/delete/<int:article_pk>/<int:comment_pk>', views.comments_delete, name='comments_delete'),
    path('<int:pk>/like_article/', views.like_article, name='like_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)