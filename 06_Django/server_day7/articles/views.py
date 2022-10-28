from django.shortcuts import render, redirect

from .forms import ArticleForm, CommentForm
from accounts.forms import CustomUserCreationForm
from .models import Article, Comment
from accounts.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)

            if article_form.is_valid():
                article_form.save()
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/update.html', context)

    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

def delete(request, pk):
    Article.objects.get(id=pk).delete()
    return redirect('articles:index')

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
    
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

def like_article(request, pk):
    article = Article.objects.get(pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    if request.user in article.like_users.all():
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고
        article.like_users.add(request.user)
    # 상세 페이지로 redirect
    return redirect('articles:detail', pk)