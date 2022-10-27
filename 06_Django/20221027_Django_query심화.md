## 2022.10.27 Django query 심화

> 이제까지 get, all만 쓰던 django query에 대한 좀 더 깊은 내용을 다룰 예정



### 📌 Django의 쿼리 동작

---

```html
{{ article for in articles }}
제목: {{ article.title }}
내용: {{ article.content }}
{{ endfor }}
```

- 상단의 코드를 실행하면 글이 총 10개가 나오는데, 내부에서 django는 몇번 쿼리문을 날릴까? -> 11번
- article 제목, 컨텐트를 가져오는 횟수 10번, 그리고 글 정렬하기 1번
- 이를 JOIN을 통해 1개 쿼리로 동작이 가능하도록 함

- N+1에 대한 문제를 해결하는 방안에 대한 고민이 필요함
- 