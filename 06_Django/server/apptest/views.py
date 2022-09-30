from django.shortcuts import render
import random

# Create your views here.
def index(request):
  # 환영하는 메인 페이지를 보여준다. /index/ 파일
  menus = ['라면', '덮밥', '돈까스']
  menu = random.choice(menus)

  context = {
    # 변수명: 값
    'name': menu,
    'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
  }
  return render(request, 'index.html', context)

def welcome(request, name):
  # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여줌

  context = {
    'name': name,
    'greetings': ['안녕하세요', 'hello', 'bon jour'],
  }
  return render(request, 'welcome.html', context)