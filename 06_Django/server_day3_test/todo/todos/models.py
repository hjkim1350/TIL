from django.db import models

# Create your models here.
class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어준다.
    content = models.CharField(max_length=80)

    # default 데이터를 생성할때 값을 안넣으면
    # 자동으로 값을 채워서 생성을 해준다.
    completed = models.BooleanField(default=False)
