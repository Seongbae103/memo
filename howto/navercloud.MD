# NaverCloud
https://parksrazor.tistory.com/854
1. 서버생성 
2. putty 사용
   - 서버생성시 만든 인증키는 putty gen, putty 사용해서 .pem 파일 .ppk로 변경
   - 근데 .com이 막혔으니까 웬만하면 집에서 하지마...

##### 2.1 Putty실행 후
   - docker 확인
     - 없으면
       - apt-get update 먼저 실행
       - apt install docker.io 실행
   - 우분투 mySQL설치
   - docker pull (DB의 도커파일에 있는 FROM)


### 우분투 mysql5.7설치
apt install -y mysql-server-5.7

---

### 참고
- '$' 사용자권한
- '#' 관리자 권한
- '$ sudo' 관리자 권한