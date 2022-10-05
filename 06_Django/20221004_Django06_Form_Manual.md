# 2022.10.04 Django06 - CRUD(POST)

>  **웹 프레임워크**
>
> 1) URL 요청을 받아서
> 2) 처리하고
> 3) 응답을 한다



> **게시판**
>
> - 생성: HTML Form, BD 저장과정
> - 조회: 글을 누르면 DB값 조회
> - 삭제: 버튼을 누르면 DB값 삭제
> - 수정: HTML Form+기존값 수정, DB 저장 과정



## 📌 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

- 가상환경 폴더를 `.gitignore`로 설정을 해둔다.

```
$ python -m venv venv
$ source venv/Scripts/activate
(venv) $
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성

```
$ django-admin startproject pjt .
```





## 📌 2. articles app

### 1. app 생성

```bash
$ django-admin startapp articles
```



### 2. app 등록

```python
# pjt/manage.py
INSTALLED_APPS = [
    'articles', # 생성한 APP 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



### 3. index.html 생성

```html
<!-- articles 밑에 templates 폴더, templates 폴더에 다시 articles 폴더 생성 -->
<!-- 위치: articles/templates/articles/index.html -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>articles</title>
</head>

<body>
  articles index.html 페이지
</body>

</html>
```



### 4. urls.py 설정

```python
# articles/urls.py 생성 후 하단 내용 생성
from django.urls import path
from . import views # 추가

app_name = 'articles'
urlpatterns = [
  	path('', views.index, name='index')
]

#-----------------------------------------------------------
# pjt/urls.py에 articles/urls.py 등록
from django.contrib import admin
from django.urls import path, include # include 포함, include 인자에 들어간 urls를 모두 참조

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



### 5. 서버 구동 테스트

``` bash
# 단축어 사용할 경우 하기와 같이 패키지 설치
$ pip install django-shortcuts

# 단축어 미 사용
$ python manage.py runserver

# 단축어 사용
$ django r
```





## 📌 3. Model 정의 (DB 설계)

### 1. 클래스 정의

- 게시판 기능
  - 제목 (20글자 이내)
  - 내용 (긴 글)
  - 글 작성시간(생성한 시점)/수정시간(마지막 업데이트 시점)

### 2. 마이그레이션 파일 생성

```python
# articles/models.py
from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=20) # 20글자 제한
  content = models.TextField() # 긴 글을 담기 위한 TextField 설정
  created_at = models.DateTimeField(auto_now_add=True) # auto_now_add: 생성한 시점
  updated_at = models.DateTimeField(auto_now=True) # auto_now: 현 시점
```



### 3. DB 반영(`migrate`)

```bash
# makemigrations
$ django mm

# migrate
$ django m
```





## 📌 4. CRUD 기능 구현

### ✏️1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)



#### 1-0. base.html 분리, index 페이지 생성

1) base.html 분리

```html
<!-- 최상위 폴더에 templates 폴더 생성 -->
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>articles</title>
</head>

<body>

</body>
{% block content %}
{% endblock %}

</html>

<!-- articles/templates/index.html -->
```



2. articles/templates/articles/index.html 수정

```html
<!-- articles/templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
<h1>게시판 페이지</h1>
{% endblock %}
```



3. articles/urls.py 수정

```python
from django.urls import path
from . import views

app_name = 'articles' # localhost:8000/articles 앱을 제어하도록 app_name 명시

urlpatterns = [
    path('', views.index, name='index'), # index 페이지 명시
]
```



4. articles/views.py 수정

```python
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'articles/index.html')
```



5. 서버 접속 테스트

```bash
# localhost:8000/articles 접속 시 생성한 index.html 내용이 출력되면 정상 설정 완료
(venv)
$ django r
```





#### 1-1. HTML Form 제공

> GET http://127.0.0.1:8000/articles/new/

##### (0) articles/index.html 수정 - 글쓰기 버튼 추가, new.html로 이동하도록 a태그 사용

```html
{% extends 'base.html' %}
{% block content %}
<h1>게시판 페이지</h1>
<a href="{% url 'articles:new' %}">글쓰기</a> <!-- a 태그 추가 -->
{% endblock %}
```



##### (1) articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), # new.html에 대한 URL 등록
]
```



##### (2) views.py

```python
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'articles/index.html')

# new 함수 정의
def new(request):

    return render(request, 'articles/new.html')
```



##### (3) articles/new.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기</h1>

<form action="{% url articles:create %}">
  <label for="title">제목: </label>
  <input type="text" name="title" id="title">

  <label for="content">내용: </label>
  <textarea name="content" id="content" cols="30" row="10"></textarea>

  <input type="submit" value="글쓰기">
</form>

{% endblock %}
```



#### 1-2. 입력받은 데이터 처리

> POST http://127.0.0.1:8000/articles/create/
>
> 게시글 DB에 생성하고 index 페이지로 redirect
>
> create.html은 별도로 생성하지 않아도 무방 - redirect 되기 때문에!

##### (1) urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # 추가
]
```



##### (2) views.py

```python
from django.shortcuts import render, redirect # redirect import 추가
from .models import Article # DB에서 데이터 가져와야 하므로 Article 클래스 가져옴

# Create your views here.

def index(request):

    return render(request, 'articles/index.html')

def new(request):

    return render(request, 'articles/new.html')

# create 생성, return은 index로 redirect
def create(request):
    # title 변수에 new.html의 form에서 submit 버튼 눌렀을 때 넘어온 데이터를 저장
    # form의 method를 별도로 지정하지 않으면 GET으로 통신
    # get 함수의 'title'은 new.html의 name="title"로 매핑된 input값이 넘어오는 것
     title = request.GET.get('title')
        
    # content라는 변수에 new.html의 form의 name="content"에서 넘어온 input값을 저장 
     content = request.GET.get('content')
    
    # Article이라는 클래스의 객체에 데이터를 create
    # Article의 title, content 컬럼에 위에서 변수로 가져온 title, content를 저장
     Article.objects.create(title=title, content=content)
    
    # create.html을 별도로 생성하지 않고 글쓰기가 완료되면 index 페이지로 넘어가도록 redirect
     return redirect('articles:index')
```



##### (3) 구동 테스트

- 글쓰기 버튼이 동작하고 index 페이지로 돌아가는지 확인



### ✏️2. 게시글 목록

> DB에서 게시글을 가져와서, template에 전달



##### (1) views.py - index 함수만 수정

```python
from django.shortcuts import render, redirect
from .models import Article

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
```



##### (2) index.html - views.py index 함수에서 return된 render 함수의 context 값을 화면에 출력

- context 값은 DB 값 전체를 가지고 있으므로, .title, .created_at 등의 컬럼명으로 제어가 가능함

```html
{% extends 'base.html' %}
{% block content %}
<h1>게시판</h1>
<a href="{% url 'articles:new' %}">글쓰기</a>

<!-- for문의 articles는 views.py에 정의한 index 함수의 return render 함수의 context 값-->
<!-- 이때 context dictionary에 articles 키를 담은 내역을 가져오는 것으로 이해 -->
{% for article in articles %}
<h3>{{ article.title }}</h3>
<p>{{ article.create_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
{% endblock %}
```



##### (3) 구동 테스트

- 글 작성 후 index 페이지에서 글 제목, 글 작성 시간, 글 마지막 수정 시간이 출력되는지 확인



### ✏️3. 상세보기

> 특정한 글을 본다.
>
> http://127.0.0.1:8000/articles/int:pk/
>
> 현재는 특정 글을 생성하거나 조회할 때 URL에 title, content 키와 데이터값을 모두 넘김
>
> 그렇게되면 URL이 너무 필요이상으로 길어지기도 하고, 조회되지 말아야할 데이터가 조회 되므로 POST 방식으로 전달 방식을 변경



##### (1) views.py - create 함수만 수정, GET에서 POST로 데이터를 가져와서 변수 title, content에 저장

```python
def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
  # redirect: URL로 다시 이동
    return redirect('articles:index')
```



##### (2) new.html

- CSRF: https://it-eldorado.tistory.com/10?category=749665
  - 로그인한 정상사용자의 글에 악성코드를 심어지게 하여 다른 희생자가 악성코드에 접근하도록 유인
- CSRF 토큰을 쓰는 이유: CSRF 공격 방지 (https://it-eldorado.tistory.com/141)
  - Django의 CSRF 토큰은 사용자의 중요 정보를 쿠키에 저장. 다른 언어나 브라우저는 세션에 저장.
  - 쿠키는 기본적으로 웹브라우저의 보안 기법 중 하나로 이를 이용하였다고 이해.

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기</h1>

<!-- method="POST" 추가-->
<form action="{% url 'articles:create' %}" method="POST">
  <!--csrf_token 추가-->
  {% csrf_token %}
  <label for="title">제목: </label>
  <input type="text" name="title" id="title">
  <hr>

  <label for="content">내용: </label>
  <textarea name="content" id="content" cols="30" row="10"></textarea>

  <input type="submit" value="글쓰기">
</form>

{% endblock %}
```



### ✏️4-1. ModelForm 적용 - new/create

> new의 기능을 create로 일원화
>
> http://127.0.0.1:8000/articles/create

##### (1) articles/form.py 생성 (https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)

- meta class는 재정의 하지 않으면 기본적으로 클래스를 만들기 위한 클래스로 정의되어 있음
  이 개념이 나올 수 밖에 없는건 class도 하나의 객체이기 때문에 class를 만들기 위한 class가 필요
- 하기 포맷은 django 공식 문서에도 보안성 향상을 위한 방법으로 제시되어 있음

```python
# django 라이브러리에서 forms 클래스 가져옴
from django import forms
# .models 라이브러리에서 Article 클래스 가져옴
from .models import Article

# class 정의
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']
```



##### (2) articles/templates/articles/index.html 수정

- ⭐ <!--<a href="{% url 'articles:new' %}">글쓰기</a>--> 을 주석 처리하고 구동하였을 때,
  계속해서 에러가 출력되어 해당 구문을 삭제하여서 에러 출력을 처리함.
- 또는 크롬 개발자 도구에서 "강력 새로고침"으로 캐시 데이터 날린 후 서버 재구동해도 동작.

```html
{% extends 'base.html' %}
{% block content %}
<h1>게시판</h1>

<!-- 하기 내용 new -> create로 수정 -->
<a href="{% url 'articles:create' %}">글쓰기</a>

{% for article in articles %}
<h3>{{ article.title }}</h3>
<p>{{ article.create_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
{% endblock %}
```



##### (3) articles/templates/articles/new.html 수정

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기</h1>

<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <!-- 추가: .as_p 옵션은 <p> 태그 안에 결과를 담는다는 의미-->
  {{ article_form.as_p }}

  <label for="title">제목: </label>
  <!-- 제일 마지막에 required 추가 -->
  <input type="text" name="title" id="title" required>

  <hr>

  <label for="content">내용: </label>
  <!-- 제일 마지막에 required 추가 -->
  <textarea name="content" id="content" cols="30" row="10" required></textarea>
  <input type="submit" value="글쓰기">
</form>

{% endblock %}
```



##### (4) articles/urls.py에서 new 삭제

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```



##### (5) articles/views.py 수정 - 함수 new 삭제, create 수정

```python
...

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

	# POST 방식으로 넘어온 데이터일 경우 is_valid()로 유효성 검사 후 index redirection
    if request.method == "POST":
        # DB 저장
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('article:index')
    
    # GET 방식으로 넘어온 데이터일 경우 기존 new 함수에서 처리하던 DB 저장 후 context 리턴
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```



### ✏️4-2. ModelForm 적용 - detail

> new의 기능을 create로 일원화
>
> http://127.0.0.1:8000/articles/int:pk/

##### (1) articles/templates/articles/detail.html 생성

```html
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>
```



##### (2) articles/templates/articles/index.html 생성

```html
<h1>게시판</h1>
<a href="{% url 'articles:create' %}">글 쓰기</a>

{% for article in articles %}
<h3>{{ article.title }}</h3>
<!-- a 링크 추가해서 제목 클릭할 경우 pk 값에 매칭되는 detail.html 페이지로 이동 -->
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
```



##### (3) articles/urls.py

```python
...

urlpatterns = [
    ...
    # 추가
    path('<int:pk>/', views.detail, name='detail'),
]
```



##### (4) articles/views.py - detail 함수 추가

```python
def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```



### ✏️5. 수정하기 (GET, POST)

> 특정한 글을 수정한다. => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)
>
> http://127.0.0.1:8000/articles/int:pk/update/



##### (1) articles/templates/articles/detail.html - 수정 버튼, 되돌아가기 버튼 추가

```html
<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>

<!-- a 링크로 글 상세 페이지에서 수정하기 추가-->
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
<a href="{% url 'articles:index' %}">메인으로 돌아가기</a>
```



##### (2) articles/templates/articles/update.html 파일 새로 생성

```html
<h1>글 수정하기</h1>

<!-- action은 별도로 지정하지 않음-->
<form action="" method="POST">
  {% csrf_token %}
   
  <!-- form의 결과를 p 태그 안에 가져오기, 이전에 썼던 데이터를 그대로 가져오는 효과 -->
  {{ article_form.as_p }}
  <input type="submit" value="수정">
</form>
```



##### (3) articles/urls.py - path 추가

```python
...
urlpatterns = [
    ...
    path('<int:pk>/update/', views.update, name='update'),
]
```



##### (4) articles/views.py - update 함수 추가

```python
def update(request, pk):
    # GET : Form을 제공
    article = Article.objects.get(pk=pk)
    article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```



----



##### (5) articles/views.py - POST 방식으로 수정

- (4)까지만 수행하면 수정된 데이터가 DB에 반영되지 않고, 유효성 검사가 되지 않음
- 이를 반영하기 위해 POST 방식으로 변경
- create 함수와 비교해보면 거의 유사함을 알 수 있음

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```





### ✏️6. 삭제하기

> 특정한 글을 삭제한다.
>
> http://127.0.0.1:8000/articles/int:pk/delete/



##### (1) articles/templates/articles/detail.html 수정

```html
{% extends 'base.html' %}
{% block content %}

<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }} </p>

<!-- 삭제하기, 메인으로 돌아가기 버튼 추가 -->
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
<a href="{% url 'articles:delete' article.pk %}">삭제하기</a>
<a href="{% url 'articles:index' %}">메인으로 돌아가기</a>

{% endblock %}
```



##### (2) articles/urls.py - path 추가

```python
...
urlpatterns = [
    ...
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```



##### (3) articles/views.py - delete 추가

```python
def delete(request, pk):
    Article.objects.get(id=pk).delete()
    return redirect('articles:index')
```

