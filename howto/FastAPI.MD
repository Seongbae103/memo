# FastAPI
>  <a href="https://github.com/Seongbae103/MSAServer/tree/main/fastApiProject">FastAPI 준비는 여기</a>
- django에서 h5를 만들고, fastAPI는 그걸 가져와서 실행하는 역할
- django는 dcoker의 사용이 선택이지만 fastapi는 필수
## 1. 실행 확인

    python -m uvicorn main:app --reload 
    또는 
    uvicorn main:app --reload

## 2. 도커 연동까지는 설정 참고

## 3. 준비
- 기본적인 틀은 <a href="https://github.com/Seongbae103/MSAServer/tree/main/fastApiProject">여기</a>를 참고<br>
<img src="C:\Users\AIA\Desktop\캡쳐\fastapi 기본 틀.PNG">

### 내용

      RUN apt update \
            && apt install -y mysql-server-5.7  \ #
            && apt install --no-install-recommends -y tzdata \ #타임존
            && apt clean




---
해설
      - (./docker/mysql/initdb.d:)/docker-entrypoint-initdb.d : (경로)에 있는 쿼리를 실행해서 db로 접근