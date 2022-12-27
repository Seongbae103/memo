## 대소문자 구분
1. 도커 시작 
- docker ps -a
- docker start containerID
- docker exec -it containerID bash
- name -U root -p
- passward
2. lower_case_table_names 확인
- db 들어가서
mydb>에 
> show variables like 'lower_case_table_names';

|variable_name|value|
|---|---|
|lower_case_table_names|0|
> 0이면 대소문자를 구분

3. 변경
- db명> exit
- apt-get update
- apt-get install -y vim
- ls
- cd etc
- ls
- cd mysql
- ls
- vim my.cnf
- 'i' 눌러서 편집 모드 전환
- [mariadb] 하단에 lower_case_table_names=1
> ※ db가 mysql이면 [mariadb]가 아니라 [mysqld]로 입력한다
- 종료: esc → ':wq!'
- 도커 다시 시작해서 ower_case_table_names 확인

## 한글 깨짐 해결
1. 도커 시작 
- docker ps -a
- docker start containerID
- docker exec -it containerID bash
- name -U root -p
- passward

2. vim 설치
- 도커 시작 후 'bash-4.2#'인 상태에서 vim 설치
  - docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.7
  - docker psdocker exec -it mysql bash
  - yum update
- yum install -y vim

3. vim으로 my.cnf 실행
- bash-4.2#에서 cd etc
- bash-4.2# ls
- vim my.cnf
- (우분투가 아니라 <a style=color:red>cent-os인 경우</a>)
    - cd /
    - ls
    - cd etc
    - ls
    - vim my.cnf
4. my.cnf 수정
- 'i'입력해서 편집 모드로 전환


    [client]와 [mysql] 는 붙여넣기
    [client] 
    default-character-set = utf8mb4 
    
    [mysql] 
    default-character-set = utf8mb4 
    
    [mysqld] 
    lower_case_table_names=1
    collation-server = utf8_unicode_ci 
    init-connect='SET NAMES utf8' 
    character-set-server = utf8
5. esc → :wq!로 나와서 다시 mysql -u root -p
6. status로 확인
    - docker ps
    - CONTAINER ID 카피
    - <a style=color:red>★</a> docker restart <CONTAINER ID> 
    - docker exec -it mysql bash
    - mysql -u root -p
    - root
    - create database mydb;
    - use mydb;
    - status
    > 
5. Db도 utf8mb4로 변경(터미널에 입력)
- use 사용할db;
- ALTER DATABASE mydb CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

### 확인
- db명>에 status; 입력
> Db, server는 utf8 / Client, Conn이 utf8mb4여야 한다
