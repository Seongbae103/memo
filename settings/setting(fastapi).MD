# FastAPI Setting

## 1. setting
- django와 같은 가상환경으로 설정하고 터미널에서 입력
#### 1.1 fastapi / uvicorn 설치

  
    - pip install fastapi 'uvicorn[standard]'
    - pip install uvicorn

#### 2. 도커 연동
- docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.7 실행
- 데이터베이스 생성
    <img src = "C:\Users\AIA\Desktop\db생성.PNG">
- docker compose up
- Test connection
  - 사용DB에 우클릭 → Properties 클릭 후 Test connection 실행
  - 실행 결과 Failed일 경우 이미지에 나온 경로에 들어가서 아래 코드 실행
    <img src="C:\Users\AIA\Desktop\grant 위치.png">
    > grant all privileges on *.* to 'root'@'%' identified by 'root'; 실행


## 3. 한글 깨짐 설정
한글 깨짐 발생시 아래 코드 입력 후 도커 이미지를 삭제하고 다시 docker compose up 실행
<img src="C:\Users\AIA\Desktop\grant 위치.png">

    chmod 644 /etc/my.cnf
    chmod 755 /etc/my.cnf
    chmod 644 /etc/mysql/conf.d/my.cnf
    chmod 755 /etc/mysql/conf.d/my.cnf

---
## Errors
#### failed to solve: rpc error: code = Unknown desc = failed to solve with frontend dockerfile.v0: failed to read docker file:
> 발생
> > compose up 실행시 발생
> 
> 해결
> > - 해결1 : Docker → Troubleshoot → Reset to factory defaults → 재실행까지 대기 후 다시 docker compose up 실행  
> > - 해결2 : 모든 이미지 삭제 후 다시 docker compose up 실행

## ???
#### docker compose up 이후 컨테이너 하나가 계속 자동 종료
> 원인
> > 은 아직 못찾았고
> 
> 해결
> > 문제있는 컨테이너가 아니라 다른 컨테이너의 컨테이너 명을 바꿔서 해결(문제 재현이 안돼서 다음에 비슷한 문제가 생기면 원인규명 필요)
