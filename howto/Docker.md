# <a href="https://github.com/Seongbae103/memo/blob/main/setting(docker).md">Docker</a>

---
### 1. DB 및 table 생성
##### (<a href ="https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ko-kr&gl=kr">터미널이 없으면 여기</a>)
- docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.7 (여기서 5.7을 빼면 최신 버전이 적용돼서 버전문제가 생긴다)
- docker ps
- docker exec -it CONTAINER ID bash
- mysql -u root(user name) -p
- password는 입력되지 않는거 같아도 되는거니까 그냥 입력
- show databases;
- create database mydb;
- use mydb;
- show tables;
- create table user( id varchar(10) primary key, password varchar(10));
- select * from user;
- insert into user values ('hong', 'pass');
- select * from user;
---
### 2. 시작할 때
- docker ps -a
- docker start containerID
- docker exec -it containerID bash
- name -U root -p
- passward
---
### 3. 컨테이너 명령어
- docker ps -a #모든 컨테이너 출력(정지 컨테이너 포함)
- docker ps #실행 중인 컨테이너만 출력
- docker start hello #hello 이름의 컨테이너 시작
- docker restart hello #hello 이름의 컨테이너 재시작(재부팅)
- docker attach hello #컨테이너에 접속(bash 쉘 접속)
- docker stop hello #hello 이름의 컨테이너 종료
- docker rm hello #hello 이름의 컨테이너 삭제
- docker rm -f hello #hello 이름의 컨테이너 강제삭제
----
### 4. 전체 날리기 
    docker system prune --all --force
---
### 5. 도커 백업 
- docker login
- docker images
- docker image tag 컨테이너명:태그명 seongbaepark/레파지토리명:1.0
- docker images
- docker push 복사된 레파지토리명:tag명
---
### 6. db테이블 자동생성
- django-admin startapp users
- cd ..
- cd dj+tab
- ls
- 생성 후 admin/setting/INSTALLED_APPS에 모듈명.파일명.파일명config -> 설정값
- models.py
> 프로젝트/admin/settings.py의 INSTALLED_APPS에 있는 모듈명.파일명.파일명config은 app에 있는 이름과 같아야 한다
> #### 예시 
> - settings에서 한번에 주고 싶으면 settings에는 blog 입력, users와 tags에는 각각 blog.users, blog.tags를 입력
※ 주의 : models.py는 자동으로 테이블을 생성해주는 파일이지만 이 과정이 아닌 수동으로 생성하거나 설정값을 주지 않으면 테이블이 생성되지 않는다

---
### 마이그레이션
- migration 폴더 안에 0001_initial.py이 없으면 
    python manage.py makemigrations
- migration 폴더 안에 0001_initial.py이 있으면
    python manage.py migrate
---
### DockerFile
- 버전 이슈에 대한 대처가 쉽다

---
## Docker 기반 Django에서 MySQL 연동으로 서버 실행
- docker ps -a
- docker image
- docler create -it 이미지명
- docker start 컨테이너명


---

## 이미지로 컨테이너 만들기
1. docker create -it 이미지
2. docker start name

---
### 방법(코드 풀이)
##### .1 루트에 Dockerfile 생성


    FROM python:3.9

    WORKDIR /django_web
    
    COPY. .
    COPY requirements.txt requirements.txt
    
    CMD ["python", "manage.py", "runserver", "0.0.0.0:!!!!"]

##### .2 docker-compose.yml 생성

    version: "3"

    services:
      databases:
        image: mysql
        container_name: 프로젝트명db (굳이 지금 쓰는 db와 같을 필요는 없다)
        volumes:
          - ~/docker/mysql/etc/mysql ('~'==현재경로/)(예시의 mysql은 앞)
          - ~/docker/var/lib/mysql:/var/lib/mysql
          - ~/docker/mysql/var/mysql:/var/log/mysql
        environment:
          - MYSQL_DATAVASE = mydb (settings.py에 있는 DATABASES의 이름)
          - MYSQL_ROOT_PASSWORD = root
          - MYSQL_ROOT_HOST = %
        command: [ '--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci' ]
      ports:
          - 3306:3306  
    web:
        container_name: 프로젝트명dj:v1
        image: seongbaepdl:v1
        build: .
        container_name: seongbaepdl:v1
        command:
          - python manage.py reunserver 0:8000
        ports:
          - "!!!!:!!!!"
        volumes:
          - .:/mydj ('.:/'==현재위치)
        expose:
          - "!!!!"  (Dockerfile의 !!!!과 같은 수)
##### .3 docker compose up


---
## 도커 에러
##### case.1 
> error during connect: This error may indicate that the docker daemon is not running.: Get "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/json?all=1": open //./pipe/docker_engine: The system cannot find the file specified.
>> 원인 : 도커 깨짐<p>
>> 해결 1 : 재설치<p>
>> 해결 2 :<p>
    sudo service docker stop<p>
    sudo rm -rf /var/lib/docker<p>
    sudo service docker start
##### case.2
> django.db.utils.OperationalError: (2002, "Can't connect to server on 'localhost' (10061)")
>> 원인 : 도커 미실행
##### case.3
> docker : The term 'docker' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1<div>
> 원인 : 인식 못함<div>
>> 해결 : 파이참 실행시 나오는 안내창 눌러주면 끝나는 문제
##### 
> DJANGO.DB.UTILS.OPERATIONALERROR: (1045, "ACCESS DENIED FOR USER 'ROOT'@'LOCALHOST' (USING PASSWORD: YES)")-MYSQL
> 원인
> >db 사용자명, 비밀번호 오류
> 
> 해결
> > settings의 databases를 참고

##### error response from daemon:
> 원인 
> >  도커 스타트 이후 ps에 실행되는 컨테이너가 없어서 시작과 동시에 꺼짐
> 해결
> > docker start 해야지...
---
## 컴포즈 에러
##### failed to solve: rpc error: code = Unknown desc = failed to solve with frontend dockerfile.v0: failed to create<br>LLB definition: dockerfile parse error line 5: unknown instruction: COPY.
> 원인
> > Dockerfile의 COPY의 공백 문제
> 
> 해결
> Dockerfile의 COPY. .을 COPY . .로 

#####
> 원인
> > 컨테이너 이름 
> 
> 해결
> > 