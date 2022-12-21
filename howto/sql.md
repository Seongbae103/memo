# SQL
 -|기능| 종류  |파이썬에서
---|---|-----|---
DDL|테이블 생성| --- |class
DML|레코드| --- |setter
DQL|관리| --- |getter

## join
    SELECT t.team_name 팀명, p.player_name 선수명, p.back_no 백넘버
    FROM team AS t
        JOIN player AS p USING(team_id)
    WHERE p.`POSITION` LIKE 'MF'
    ;
### TX
> select를 여러번 사용하는 경우를 한번의 select로 해결가능
- join은 한 번에 한다기 보다 그 숫자만큼 select

### thread (실행중인 메소드)
- 디스크에서 프로그램, 메모리에서는 프로젝트

## SubQuery
> 일괄 처리를 위한 쿼리 안의 또 다른 쿼리
    <p>SELECT col1, (SELECT~) -> 스칼라(하나의 컬럼처럼 사용)
    <p>FROM(SELECT~) -> 인라인 뷰(하나의 테이블처럼 사용)
    <p>WHERE col=(SELECT~) -> 서브쿼리(하나의 변수처럼 사용)
>> Scalar > Sub Query > Inline View > join 순으로 효율이 좋다 
### 종류
- Sub Query
- Inline View
- Scalar

---
예제 (줄바꿈은 알아서)
> 카티션 체크
>> SELECT COUNT(*)
    FROM team AS t
        JOIN player AS p USING(team_id); 
<P>> 이거 아니어도 join가서 using 체크
1. 삼성블루윙즈 팀아이디는 무엇인가 ?
2. 전체 축구팀의 목록을 출력하시오 <div>(단, 팀명을 오름차순으로 정렬하시오.)
3. 포지션의 종류를 모두 출력하시오 <div>(단, 중복은 제거합니다.)
4. mysql 에서 case 문 이용해서 다음 문제를 해결하세요
   - 포지션의 종류를 모두 출력하시오
   - 단, 중복은 제거합니다. 
   - 포지션이 없으면 신입으로 기재
5. 다음 조건을 만족하는 선수명단을 출력하시오(join 사용 x)
   - 소속팀이 삼성블루윙즈이거나
   - 드래곤즈에 소속된 선수들이어야 하고,
   - 포지션이 미드필더(MF:Midfielder)이어야 한다.
   - 키는 170 센티미터 이상이고 180 이하여야 한다.
6. 2012년 3월 17일 경기에 포항 스틸러스 소속 골키퍼(GK) 선수, 포지션,팀명 (연고지포함), 스타디움, 경기날짜를 구하시오 연고지와 팀이름은 간격을 띄우시오(수원[]삼성블루윙즈)
7. 포지션이 MF 인 선수들의 소속팀명 및  선수명, 백넘버 출력
8. 가장 키큰 선수 5명 소속팀명 및  선수명, 백넘버 출력<div>(단 키  값이 없으면 제외)
9. 2012년 5월 한달간 경기가 있는 경기장  조회
10. 수원을 연고지로 하는팀의 골키퍼는 누구인가 ?
11. 수원 연고팀에서 키가 170 이상 선수이면서 성이 고씨인 선수는 누구인가
---
### SQL문
##### left(right) join
- null 값도 남기고 싶으면 null이 있는 컬럼에 따라 left(right) 결정 <p> -> 가독성을 고려해서 left를 더 많이 쓴다
##### Group By 
> 클러스터링<p>
>> 열을 줄이는 차원 축소와 다르게 행을 줄인다  
---
## 판다스db mysql로
### db연결
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd
    db_connection_str = 'mysql+pymysql://[db유저이름]:[db password]@[host address]/[db name]'
    db_connection = create_engine(db_connection_str)
    conn = db_connection.connect()
### db저장
    df.to_sql(name='db의 테이블이름', con=db_connection, if_exists='append',index=False)  

참고 : <a>https://data-make.tistory.com/25
    