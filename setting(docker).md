# 도커 설치
### <a href> https://www.docker.com/products/docker-desktop/ </a>
### 터미널에 입력
> 터미널 설치 : <a href> https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ko-kr&gl=kr

01. docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.6
02. docker ps
03. docker exec -it CINTAINER ID bash
04. mysql -u root(user name) -p
05. password는 입력되지 않는거 같아도 되는거니까 그냥 입력
06. show databases;
07. create database mydb;
08. use mydb;
09. show tables;
10. create table user( id varchar(10) primary key, password varchar(10));
11. select * from user;
12. insert into user values ('hong', 'pass');
13. select * from user;
---
# 하이디 설치
> <a href>https://www.heidisql.com/
- 인스톨러 -> mydb
---
# docker 대소문자 구분 안하는 설정
01. docker ps -a
02. docker start 이름
03. docker exec -it 이름 bash
4. 이름 -u root -p
5. 패스워드
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
<img src="C:\Users\AIA\Desktop\잡\ls.png">
---
# 시작할 때
- docker ps -a
- docker start NAME