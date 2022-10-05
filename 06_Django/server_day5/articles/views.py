from django.shortcuts import render, redirect

import articles
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
  # DB에서 가져온 Article 객체를 생성된 역순(pk번호 역순)
    articles = Article.objects.order_by('-pk')
  
  # templates에 전달 - 위에서 articles라는 변수에 담은 dictionary
  # dictionary 형태로 정의하는 이유는, render() 함수의 정의 때문임
  # render: 템플릿을 불러옴
  # render 함수 정의: render(request, template_name, context=None, content_type=None, status=None, using=None)
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

# def new(request):
    # article_form = ArticleForm()
    # context = {
    #     'article_form': article_form
    # }
    # return render(request, 'articles/new.html', context)

def create(request):
  #   # title = request.GET.get('title')
  #   # content = request.GET.get('content')
  #   title = request.POST.get('title')
  #   content = request.POST.get('content')
  #   Article.objects.create(title=title, content=content)
  # # redirect: URL로 다시 이동
  #   return redirect('articles:index')
    if request.method == "POST":
        # DB 저장
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    # pk에 매칭되는 글을 가져옴
    article = Article.objects.get(pk=pk)

    # template에 객체 전달
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    # POST 데이터 처리
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    Article.objects.get(id=pk).delete()
    return redirect('articles:index')