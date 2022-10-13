## 2022.10.11 Django08



### 📌Django Auth

---

- 인증 시스템은 인증과 권한 부여를 함께 처리하고 있음

- 인증(Authentication): 신원 확인, 사용자가 누구인지 확인하는 과정

- 권한, 허가(Authorization): 인증된 사용자가 수행할 수 있는 작업의 범위

- 필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능
  - django.contrib.auth

- account app 생성 및 등록

  ```python
  $ python manage.py startapp accounts
  
  # settings.py
  INSTALLED_APPS = [
      ....
      'accounts',
      ....
  ]
  ```

  

- DB 생성하게되면 DB안에 auth_user 테이블이 이미 생성되어 있는데, 이 테이블 안에 admin 등의 계정정보를 저장함 (https://docs.djangoproject.com/en/4.1/ref/contrib/auth/)

  ```bash
  # 하기와 같은 명령어로 슈퍼유저를 생성하면 localhost:8000/admin에서 로그인할 수 있음
  # 이 admin에 관련된 계정들이 db.sqlite3 내 auth_user table로 관리되고 있음
  
  $ python manage.py createsuperuser
  
  ```

  

- 따라서 Django는 새 프로젝트를 시작할 경우 위와 같이 db.sqlite3 내에 정의된 User 모델이 충분하더라도 커스텀 User 모델로 설정하는 것을 강력하게 권장

  (https://docs.djangoproject.com/en/4.1/ref/contrib/auth/)

  - 이미 APP이 많이 개발된 상태에서 DB 구조 자체를 변경하기 쉽지 않기 때문

  - 또한 Django의 User Model은 기본적으로 username을 식별값으로 사용하기 때문에 식별값을 이메일이나 다른 키값으로 가져가야하는 경우 커스텀 User 모델로 가져가야 함

  - 하기 코드의 AUTH_USER_MODEL 값은 global_settings.py 상속받아 재정의하여야 함

    ```python
    # settings.py
    
    AUTH_USER_MODEL = 'accounts.User'
    ```

  - 관련하여서는 django의 공식 GITHUB를 참고하여야 함

    - https://github.com/django/django/blob/main/django/conf/global_settings.py

- User 모델 상속 관계

  - AbstractBaseUser - 비밀번호/인증
  - class AbstractUser - username 등 - 필요할 경우 custom 하는 부분
  
  ```python
  # accounts/models.py
  # 원래 models.py도 직접 필드를 지정하여 정의하였는데, AbstractUser라는
  # 기존에 만들어진 포맷을 가져와서 사용!
  
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  # Create your models here.
  class User(AbstractUser):
    pass
  ```
  
- 생성되었었던 db.sqlite3 삭제 후 makemigrations - migrate 작업 수행

- 그러고 난 후 superuser를 다시 생성하고 open database를 실행하게 되면,
  accounts_user 테이블에 생성한 superuser 정보가 담기는 것을 볼 수 있음

- 그 외에 관련 메서드 등을 보려면 공식문서 참조

  - https://github.com/django/django/blob/main/django/contrib/auth/models.py

- django에서 정의한 DB를 커스텀하게 되면 비밀번호 구현 등 복잡한 구현을 쉽게 가져다가 쓸 수 있음



## 📌User model 활용하기

- 회원 가입시 암호를 반드시 단방향 암호화하여 저장하여야 함

- password 관련 단방향 암호화 등을 django에서 지원을 해주고 있음

  - https://docs.djangoproject.com/en/4.1/topics/auth/passwords/

- 유저 생성 테스트

  ```bash
  $ python manage.py shell_plus
  
  In[1]: User.objects.create_user('hong', 'hong@gmail.com', '1q2w3e')
  
  # accounts_user에 비밀번호가 암호화되어서 들어가있는 것을 확인할 수 있음
  ```

  



## 💡참고 - ORM 설치

- django-extensions 설치

- ```bash
  $ pip install django-extensions
  $ pip install ipython
  ```

- app 등록

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      ...
      'django_extensions',
      ...
  ]
  ```

- APP 실행

  ```bash
  $ python manage.py shell_plus
  ```



## 📌회원가입 페이지 만들기

- accounts/urls.py

  ```python
  # accounts/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
  ]
  ```

  

- accounts/views.py

  ```python
  # accounts/views.py
  
  from django.shortcuts import render
  
  # Create your views here.
  def signup(request):
      return render(request, 'accounts/signup.html')
  ```

  

- accounts/templates/accounts/signup.html

  - 결국 user와 연결된 모델form이 필요함 > views.py에서 auth form을 import 받아 처리
  - 그리고 form을 출력할 때 영어가 나오면 settings.py에서 LANGUAGE_CODE = 'ko-kr' 변경

  ```html
  <!-- accounts/templates/accounts/signup.html -->
  
  {% extends 'base.html' %}
  {% block body %}
  <h1>회원가입</h1>
  {{ form.as_p}}
  {% endblock%}
  ```

  

- accounts/views.py 수정

  ```python
  # accounts/views.py 
  
  from contextlib import redirect_stderr
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import UserCreationForm
  
  # Create your views here.
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form':form
      }
      return render(request, 'accounts/signup.html', context)
  ```



- bootstrap 적용

  - django-bootstrap 관련 공식 문서: https://django-bootstrap5.readthedocs.io/en/latest/

  ```bash
  $ pip install django-bootstrap5
  ```

  ```python
  # settings.py
  INSTALLED_APPS = [
      ...
      'django_bootstrap5',
  ]
  ```

  ```html
  <!-- base.html -->
  <head>
      <!-- Css -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-uWxY/CJNBR+1zjPWmfnSnVxwRheevXITnMqoEIeG1LJrdI0GlVs/9cVSyPYXdcSF" crossorigin="anonymous">
  
  <!-- Javascript -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-kQtW33rZJAHjgefvhyyzcGF3C5TFyBQBA13V1RKPf4uH+bwyzQxZ6CmMZHmNBEfJ" crossorigin="anonymous"></script>
  </head>
  ```

  ```html
  <!-- accounts/templates/accounts/signup.html -->
  {% extends 'base.html' %}
  {% load django_bootstrap5 %} // 추가
  
  {% block body %}
  <h1>회원가입</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %} // django-bootstrap 문법에 맞춰 출력 
    {% bootstrap_button button_type="submit" content="OK" %}
  </form>
  
  {% endblock body%}
  ```



- 이 단계까지 하고 회원가입 페이지에서 회원정보를 입력하고 가입 버튼을 누르면 에러페이지가 출력됨

  ```html
  AttributeError at /accounts/signup/
  Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
  ```

- 이것에 대한 해답은 django Github>contrib>auth>forms.py에서 찾을 수 있음

  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py

- views.py에서 정의하였던 UserCreationForm을 찾아보면 class UserCreationForm(forms.ModelForm):로 정의되어 있는데, 이 class는 ModelForm을 인자로 받아오고, 이 인자가 동작하는 이유는 상단에 from django.contrib.auth.models import User 으로 상속받기 때문임.

- 그러면 이 ModelForm을 가져오기 위해서는 accounts/forms.py 생성하여야 함

  ```python
  # accounts/forms.py
  
  from django.contrib.auth.forms import UserCreationForm
  from .models import User
  
  # 그 전에는 class ArticleForm(forms.ModelForm) 등 모델로부터 직접 상속 받았다면,
  # 지금은 UserCreationForm이라는 기존에 만들어진 폼만 가져와서 사용하는 구조로 작성됨!
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta:
          model = User
  #        fields = '__all__'
          fields = ('username', )
  ```

  

- 이 model form에서 생성한 내역을 상속받기 위해 views.py를 다음과 같이 수정

  ```python
  # accounts/views.py
  
  from contextlib import redirect_stderr
  from django.shortcuts import render, redirect
  # from django.contrib.auth.forms import UserCreationForm
  from .models import CustomUserCreationForm 
  
  # Create your views here.
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form':form
      }
      return render(request, 'accounts/signup.html', context)
  ```



- 이 단계까지 오게되면 회원 관련 모든 폼을 제어하는 페이지가 출력됨, forms.py에 fields에서 all로 가져오기 때문임.

  - fields = ('username', ) 등 필요한 부분만 발췌하여 구동

- admin 페이지에서 관리하려면 하기와 같이 수정

  ```python
  # accounts/admins.py
  
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  # Register your models here.
  admin.site.register(User, UserAdmin)
  ```



- django 문서에 따르면, AUTH_USER_MODEL을 사용할 경우 User를 직접 참조하기 보다는 django.contrib.auth.get_user_model()을 사용하는 것이 더 좋다고 함.

- 따라서 하기와 같이 admins.py를 수정

  ```python
  # accounts/admins.py
  
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  #from .models import User
  from django.contrib.auth import get_user_model
  
  # Register your models here.
  admin.site.register(get_user_model(), User, UserAdmin)
  ```

- 그리고 forms.py도 하기와 같이 수정

  ```python
  # accounts/forms.py
  
  from django.contrib.auth.forms import UserCreationForm
  #from .models import User
  form django.contrib.auth import get_user_model
  
  
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta:
  #        model = User
  		model= get_user_model()
          fields = ('username', )
  ```



## 📌프로필 페이지 만들기

- 프로필 페이지 만들기 위해 고려할 것?

  - URL 어떻게 정의할지? /accounts/2/
  - View: detail
  - Template 반환: 사용자정보(username)

- URL 만들기 

  ```python
  # accounts/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
      path('<int:pk>/', views.detail, name='detail'), # 추가
  ]
  ```

- 기능 만들기

  ```python
  # accounts/views.py
  
  # User 직접 참조는 하지 않고 get_user_model을 사용하기로 하였으니 하기와 같이 import 수정
  # from accounts.models import User
  from django.contrib.auth import get_user_model
  ...
  
  def detail(request, pk):
      user = get_user_model().objects.get(pk=pk)
      context = {
          'user': user
      }
      return render(request, 'accounts/detail.html', context)
  ```

- html 만들기

  ```html
  <!-- accounts/templates/accounts/detail.html-->
  
  {% extends 'base.html' %}
  {% block body %}
  <h1>{{ user }}님의 프로필</h1>
  {% endblock body %}
  ```

  

### 💡참고 - 비밀번호 검증?

---

- 회원가입 포맷 양식 안에 비밀번호, 비밀번호 확인 input이 정의되어 있음.
- 비밀번호/비밀번호 확인 입력 값이 맞는지 확인하고, 비밀번호 정책에 부합하는지도 검증함
- django Github > contrib > auth > forms.py 문서에서 def clean_password2를 보면 이 로직이 들어가있음.
  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py



### 💡참고 - contrib이란?

---

- https://docs.djangoproject.com/en/4.1/ref/contrib/
  - django가 도와주는 기능의 총집합이라고 보면됨
  - 일반적인 기능들도 담긴 패키지명이라고 인식!