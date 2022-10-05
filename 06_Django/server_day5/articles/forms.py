# django 라이브러리에서 forms 클래스 가져옴
from django import forms
# .models 라이브러리에서 Article 클래스 가져옴
from .models import Article

# class 정의
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']