## 2022.10.21 실습 - 수람, 동현, 현정

1. **일시**: 2022.10.21 09:30 ~ 17:30

2. **프로젝트 참여자**: 조수람, 이동현, 김현정

3. **폴더 구조 및 기능 **

   ```text
   venv (가상환경)
   ------------------------------------------------
   config (프로젝트)
    ㄴ articles (게시판)
       - CRUD
       - 댓글
       - 글 작성자만 수정/삭제하도록 권한 할당
    ㄴ accounts (계정 관련)
       - 회원가입
       - 로그인, 로그아웃
       - 회원정보 수정
       - 패스워드 변경
       - 회원 프로필(내가 쓴 게시글 총 갯수, 게시글 내용, 댓글 총 갯수, 댓글 내용)
    ㄴ medias (미디어 파일 관련 - 아이디어 차용 인스타?)
       - 이미지 업로드
       - 동영상 업로드: 유튜브
   ```



4. **초기 세팅**

   - git repo 생성, 팀원 초대, 가상환경 생성

   - .gitignore 생성

     - https://www.toptal.com/developers/gitignore/
   - python, windows, mac, django, VisualStudioCode 추가 후 ignore 파일 생성
     
   - requirements.txt 생성
     
       - 설치 패키지

         [1] django == 3.2.13

         [2] django-bootstrap5

         [3] django-shortcuts

         [4] image-kit

         [5] pillow

         [6] django-messages

   - 프로젝트/앱(articles, accounts), base.html, static 생성

   - pjt/settings.py, pjt/urls.py 설정 및 static 폴더 생성