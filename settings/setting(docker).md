# Docker
### 1. 설정 과정   
db -> app-> middleware

### <a href="https://learn.microsoft.com/ko-kr/dotnet/architecture/microservices/multi-container-microservice-net-applications/multi-container-applications-docker-compose">컴포지트</a>
> 여러개의 컨테이너가 필요할 때 사용
- yaml
### 1.1 설치
- <a href="https://www.docker.com/products/docker-desktop/">도커 설치</a>
- <a href = "https://learn.microsoft.com/ko-kr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package">x64 머신용 WLS2 Linux 커널 업데이트 패키지 다운로드 및 설치 </a>
※ 파이참에서 도커 사용시 기본 터미널을 cmd가 아닌 powershell로ㅡ 이용
---
# 2. 하이디 설치
> <a href>https://www.heidisql.com/
- 인스톨러 -> mydb
---

# 3. docker 대소문자 구분 안하는 설정
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
# errors
### 1. This error may indicate that the docker daemon is not running
> 해결 <img src="C:\Users\AIA\Downloads\de.png">

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
 docker Image가 Alpine인 경우 /bash 대신 /sh를 사용

