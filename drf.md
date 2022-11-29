# <a style = color:red>D</a>jango <a style = color:red>R</a>est <a style = color:red>F</a>ramework
### ※ PowerShall 관리자권한으로 실행 
    cd (파일경로)
    mkdir (프로젝트명)
    cd d(탭 gksqjs)
    pip install django
    pip install djangorestframework
    pip install markdown
    django-admin startproject admin .
    django-admin startapp hello
    python manage.py migrate
    python m (만 치고 탭키) createsuperuser --email (본인이메일) --user (본인아이디)
    python m (만 치고 탭키) runserver
    http://127.0.0.1:8000 Ctrl + 클릭
    확인 후 ctrl + c로 종료
---
## 설정시 문제
### error1
<img src="C:\Users\AIA\Desktop\e_dj.png"><p>
> 원인 : 관리자 권한이 아닌 상태에서 설치했을 경우 발생하는 문제
>> 해결 : pip uninstall 'django, djangorestframework 등' 으로 삭제 후 관리자 권한으로 다시 설치
---