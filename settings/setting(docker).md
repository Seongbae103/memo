# Docker
### 1. 설치
- <a href="https://www.docker.com/products/docker-desktop/">도커 설치</a>
- <a href = "https://learn.microsoft.com/ko-kr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package">x64 머신용 WLS2 Linux 커널 업데이트 패키지 다운로드 및 설치 </a>
### 2. 터미널에 입력
> <a href ="https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ko-kr&gl=kr">터미널 설치 후 입력</a>
- docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.7
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
※ 파이참에서 도커 사용시 기본 터미널을 cmd가 아닌 powershell로ㅡ 이용
---
# 하이디 설치
> <a href>https://www.heidisql.com/
- 인스톨러 -> mydb
---
# 시작할 때
- docker ps -a
- docker start containerID
- docker exec -it containerID bash
- name -U root -p
- passward
---
# docker 대소문자 구분 안하는 설정
01. 파워쉘에서 도커 시작
6. show variables like 'lower_case_table_names';
> <a style = color:red>값이 0이면 대소문자 구분, 1이면 구분x</a>
07. exit
8. 유저명@컨테이너_id:/# ls
9. 유저명@컨테이너_id:/# cd etc
9. 유저명@컨테이너_id:/etc# ls
9. 유저명@컨테이너_id:/etc# cd etc
9. 유저명@컨테이너_id:/etc/이름#/ls
9. 유저명@컨테이너_id:/etc/이름#/vim my.cnf
10. i 입력으로 insert 전환
11. [db명d]
12. lower_case_table_names=1
07. 다시 시작
8. 
<img src="C:\Users\AIA\Desktop\잡\ls.png">
---
## 이미지로 컨테이너 만들기
1. docker create -it 이미지
2. docker start name
---
# error
### 1. This error may indicate that the docker daemon is not running
> 해결 <img src="C:\Users\AIA\Downloads\de.png">
> 
### 2. WSL 2 installation is incomplete
> 해결
> - 도커 삭제
> - 리눅스 서브시스템 활성 명령어 입력
> > dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
>
> - 가상머신 플랫폼 기능 활성화 명령어 입력
> > dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
>  
> - 도커 재설치
> - x64 머신용 WLS2 Linux 커널 업데이트 패키지 다운로드 및 설치(윗 내용 참고)
### 3. OCI runtime exec failed: exec failed:
