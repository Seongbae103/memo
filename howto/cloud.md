# 클라우드
___
## 목차
#### 1.설정하기
##### 1.1 DB설치
#### 2.

___
## 1. 설정하기
###  1.1 DB설치
- 일단 오늘은 가상이 아니라 마리아DB사용
  - 설치 : <a href>https://mariadb.com/downloads/
    <p> 주의사항 : 'use UTF8', 'Enable access from remote machines~'체크
  - 환경변수 설정 
    - 'window+"r"'
    - 'sysdm.cpl ,3' -> 기억 안나면 아나콘다 환경설정 참고
    - 버전 확인
<p>

- Windows termunal 설치
  - 터미널에서 다음 순서로 입력
      - mysql -u root -p
      - root
      - use mysql
      - create database mariadb;
      - show databases;
      - use mariadb
      - create user 'mariadb'@'localhost' identified by 'mariadb';
      - grant all privileges on mariadb.* to mariadb@localhost;
      - flush privileges;
      - exit;
