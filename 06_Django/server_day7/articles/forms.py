from socket import fromshare
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image',)
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '이미지 업로드',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('com_content',)
        labels = {
            'com_content': '댓글',
        }