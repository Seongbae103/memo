# Docker
##### - <a href="https://github.com/Seongbae103/memo/blob/main/setting(docker).md">설치</a>
## 시작할 때
- docker ps -a
- docker start containerID
- docker exec -it containerID bash
- name -U root -p
- passward
- 
### 컨테이너 명령어
- docker ps -a #모든 컨테이너 출력(정지 컨테이너 포함)
- docker ps #실행 중인 컨테이너만 출력
- docker start hello #hello 이름의 컨테이너 시작
- docker restart hello #hello 이름의 컨테이너 재시작(재부팅)
- docker attach hello #컨테이너에 접속(bash 쉘 접속)
- docker stop hello #hello 이름의 컨테이너 종료
- docker rm hello #hello 이름의 컨테이너 삭제
- docker rm -f hello #hello 이름의 컨테이너 강제삭제


### 마이그래이션
    python manage.py makemigrations
    python manage.py migrate

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

