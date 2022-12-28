# <a style = color:red>D</a>jango <a style = color:red>R</a>est <a style = color:red>F</a>ramework
### ※ PowerShall 관리자권한으로 실행 
    cd (파일경로)
    mkdir (프로젝트명)
    cd d(탭 한번)
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

### mysql 연동
- 파이참 데이터베이스에서 '+' 아니면 도커 에러 케이스3대로 해결
- admin의 settings.py에서 데이터베이스 수정<p>
> DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'mydb',
          'USER': 'root',
          'PASSWORD':'root',
          'HOST':'127.0.0.1',
          'PORT':'3306'
      }
  }
- settings에 추가
    CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000'
                         ,'http://localhost:3000']
    CORS_ALLOW_CREDENTIALS = True
##### 서버실행
- docker create -it 이미지명
- docker start 컨테이너명
- docker run 컨테이너명
### db테이블 자동생성
- django-admin startapp users
- cd ..
- cd dj+tab
- ls
- 생성 후 admin의 setting에서 INSTALLED_APPS에 모듈명.파일명.파일명config -> 설정값
- models.py
※ 주의 : models.py는 자동으로 테이블을 생성해주는 파일이지만 이 과정이 아닌 수동으로 생성하거나 설정값을 주지 않으면 테이블이 생성되지 않는다

---
## 장고, 리액트 연결
### 1) 리액트에서 준비
- src/폴더에 
  

    api의 index.js
    import axios from "axios";
    const server = `http://127.0.0.1:8000`
    export const strokeapi = req => axios.get(`${server}파이참 내의 url에서 지정한 경로/url에서 지정한 이름`, req)
<br/>

    components의 .jsx
    import { strokeapi } from "blog/api"

    const Stroke = () => {
        const onClick = e =>{
            e.preventDefault()
            strokeapi() /**api index에서 export한 주소를 받아준다*/
        }
        return (
        <>
        <button onClick={onClick}> 실행 </button>
        </>
        )}
    export default Stroke
<br/>

    폴더의 index.js
    export {default as 파일명} from "파일 경로/파일명"

### 2) 장고에서 연결


---
## 설정시 문제
##### error1
> django-admin : The term 'django' is not recognized~<p>
> 원인 : 관리자 권한이 아닌 상태에서 설치했을 경우 발생하는 문제
>> 해결 : pip uninstall 'django, djangorestframework 등' 으로 삭제 후 관리자 권한으로 다시 설치
##### case.2
Error response from daemon

##### case.3


---
