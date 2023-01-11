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
- VO = model
  - DAO는 항상 차있는 상태
- DAO = repasitories
- DTO = schemas
  - 리액트와 연결되는 지점
  - DTO는 항상 비어있는 상태여야한다
### 내용

      RUN apt update \
            && apt install -y mysql-server-5.7  \ #
            && apt install --no-install-recommends -y tzdata \ #타임존
            && apt clean



###
 로그인은 세션을 생성
---
해설
      - (./docker/mysql/initdb.d:)/docker-entrypoint-initdb.d : (경로)에 있는 쿼리를 실행해서 db로 접근

      
      @app.get("/items/languges/{item_id}") #{item_id}는 request에 id를 부여 (단, id가 없는 create, all 등의 경우는 없다)


---
# error
### RuntimeError: no validator found for <class 'sqlalchemy.sql.schema.Column'>, see `arbitrary_types_allowed` in Config
### ModuleNotFoundError: No module named 
> 상황
> > pip install로 설치 후 import를 했지만 위의 에러가 발생
> 
> 원인
> > requirements.txt 파일이 있는 경우 해당 파일에 install한 패키지를 입력하지 않아서 발생
> 
> 해결
> > requirements.txt에 설치한 패키지 추가

###  2023-01-09T07:57:16.111411Z 3 [Note] Aborted connection 3 to db: 'mydb' user: 'root' host: '172.20.0.1' (Got an error reading communication packets)

### 썼는데 안먹어...
> 해결
> > fastapi는 async를 써야지...

### pymysql.err.OperationalError: (2013, 'Lost connection to MySQL server during query')
> 원인
> > 
> 
> 해결
> > my.cnf파일의 mysqld에 다음코드 추가<br>
> > max_allowed_packet=16M

###  fastapi.exceptions.FastAPIError: Invalid args for response field! Hint: check that <class ''> is a valid Pydantic field type
> 원인 
> > 에러창에 나온 그대로다
> 해결
> 클래스 내부에 아래 클래스 두 개중 하나 입력(경우에 따라 안먹는 경우가 있어서 바꿔주면서 적용)
    class Config:
        BaseConfig.arbitrary_types_allowed = True

    class Config:
        arbitrary_types_allowed = True
