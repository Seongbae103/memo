# Docker
##### - <a href="https://github.com/Seongbae103/memo/blob/main/setting(docker).md">설치</a>
### db테이블 자동생성
- django-admin startapp users
- cd ..
- cd dj+tab
- ls
- 생성 후 admin의 setting에서 INSTALLED_APPS에 모듈명.파일명.파일명config -> 설정값
- models.py
※ 주의 : models.py는 자동으로 테이블을 생성해주는 파일이지만 이 과정이 아닌 수동으로 생성하거나 설정값을 주지 않으면 테이블이 생성되지 않는다


### 마이그래이션
    python manage.py makemigrations
    python manage.py migrate