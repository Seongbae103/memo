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
- yum install -y vim

3. vim으로 my.cnf 실행
- bash-4.2#에서 cd etc
- bash-4.2# ls
- vim my.cnf

4. my.cnf 수정
- 'i'입력해서 편집 모드로 전환

5. Db도 utf8mb4로 변경(터미널에 입력)
- ALTER DATABASE mydb CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

### 확인
- db명>에 status; 입력
> Db, Client, Conn이 utf8mb4여야 한다
