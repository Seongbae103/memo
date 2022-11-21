# 도커 설치
## <a href> https://www.docker.com/products/docker-desktop/ </a>
## 지시대로 설치
### 터미널에 입력
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
### 하이디 설치
<a href>https://www.heidisql.com/
- 인스톨러 -> mydb

