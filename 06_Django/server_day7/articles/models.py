from pyexpat import model
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이미지 업로드
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(300,300)],
        format='PNG',
        options={'quality': 90},
    )

# 댓글
class Comment(models.Model):
    com_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)