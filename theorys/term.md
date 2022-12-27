# 1. DcGan
> Deep Convolutional Generative Adversarial Networks

# 2. ML / DL
> nn(신경망)의 유무에 따라 : DL / ML 
> ML = DL + 확률
> ML이 DL보다 넓은 개념
- 묵시적
- 샘플데이터를 기반으로 모델 구축
  - (샘플 데이터 = 훈련 데이터)
- ML과 DL 차이점은 통계다 
  - ML은 통계학습
### MSE vs. CCEE
회귀ML의 손실함수는 MSE
분류ML의 손실함수는 CCEE(Categorical Cross Entropy Error), 활성화 함수로 softmax를 사용한다

# 3. 데이터 유형
> 이산형(Categorical)
>> 명목(norminal), 순위(ordinal) 
> 
> 연속형(Continuous)
>> 간격(Interval), 비율(Ratio)

## 인코딩(encoding) ↔ 디코딩(decoding) (플로우가 보이는 머신러닝 프로젝트 p.384)
> 문자 → 숫자

### one-hot encoding
> 

## 데이터 분석의 두 가지 접근 방법
1) 확증적 데이터 분석(<a style=color:purple>CDA</a>: Confirmatory Data Analysis) = 추론통계 = (가설 → 특정사례) = 연역
2) 탐색적 데이터 분석(<a style=color:purple>EDA</a>: Exploratory Data Analysis) = 기술통계 = (데이터(특정사례) → 모델) = 귀납 (캐글 데이터셋 페이지에 나온 그래프처럼 표현된게 EDA)
> 인공지능은
>> 지도 : 귀납 → 연역 / 비지도 : 연역 → 연역
> 
>> 지도와 비지도의 차이는 연역과 귀납 중 무엇으로 시작하는지다

세상에 없는걸 만들면 ML, 이미 있는걸 다시 확인하면 통계
### 연역과 귀납
- 연역은 가정된 전제이다.
- 귀납은 개인적 경험이다.
### 확률(prob)
- 종류
  - 수학적(선험적) 확률(시작점이 가설) → 사전 : 식으로 존재 → 연역
  - 통계적(경험적) 확률(시작점이 데이터) → 사후 : 식*큰수(data, limit) → 귀납
- 큰수의 법칙 
> 수학적 확률과 통계적 확률이 같아지는 지점이 있다는게 대수법칙
> P(A) = lim(k/n)에서 P(A)는 통계적, 계수lim은 통계적 확률, k/n은 수학
> 로그는 큰 수다 (log2 1024=10에서 10은 log2를 생략하고 1024를 나타내서)
- target(기대값) = 계수 * variable(변수) + constant(상수)
### 통계
> 데이터 + 확률 
### ML을 위한 통계 개념
표본<br/>
우도함수

    > 우도 함수(가능도 함수로 번역되기도 하고, 영어로는 likelihood function 이라 합니다)는 실현된 데이터(혹은 관찰된 데이터 observed data)로 부터 특정 통계 모델의 적합성을 확인하는데 주로 이용됩니다.

대수(큰 수)의 법칙<br/>
베이지안<br/>
분포<br/>
랜덤
### 추론과 예측의 차이는
- 예측(Predict) : 결정론적 알고리즘을 통한 이미 정해진 답을 맞추는 행위
- 추론(Inference) : '대체로 이렇다'라는 미래에 대한 답을 도출하는 행위</br>
 <a style=color:violet>예측은 학습이고 추론은 모델을 돌린 결과</a>
- 역연역


### Ground Truth(모자 벗은 Y)
https://mac-user-guide.tistory.com/14
https://towardsdatascience.com/in-ai-the-objective-is-subjective-4614795d179b
개발자가 원하는(보고 싶은) 답 → 개발자가 줘야한다
정답지인 label과 같을 필요는 없다

### 정규화(Normalization)와 표준화(Standardization = Z-score)
> feature의 변환은 정규화와 표준화가 있다
> 아웃라이어가 있으면 표준화, 나머지는 정규화가 낫다
- 정규화는 이상치 제거x, 표준화는 이상치를 제거한 형태

### 오차, 편차, 잔차
- 편차(Deviation) : 예측값(타깃값,y^)평균에서 예측값이 떨어진 정도(영점 맞춘다고 생각)
- 오차(Error) : 실제값(y)과 예측값(y^)의 차이
- 잔차(Residual) : 실제값과 트레인 단계의 예측값
> 트레인 단계에서는 잔차를 줄이고, 테스트에서는 오차를 줄여야 한다.

### 편향과 편차, 분산
<a href="https://opentutorials.org/module/3653/22071">링크</a><br/>
정답 하나를 맞추기 위해 컴퓨터는 여러 번의 예측값 내놓기를 시도하는데,
컴퓨터가 내놓은 예측값의 동태를 묘사하는 표현이 '편향' 과 '분산'이다

예측값들과 정답이 대체로 떨어져 있으면 결과의 편향(bias)이 높다고 말하고,
예측값들이 자기들끼리 대체로 흩어져있으면 결과의 분산(variance)이 높다고 말합니다.

회귀 문제이든, 분류 문제이든
첫 번째 그림과 같은 상황을 Underfitting = High Bias<br/>
세 번째 그림과 같은 상황(y와 y Hat이 완전 일치)을 Overfitting = High Variance라고 한다
> 오버피팅의 경우는 맞춘게 아니라 답을 알고있었다고 해서 오히려 안좋은 상황이다 95%가 가장 이상적이다

#### 분산과 표준편차
> 표준편차 : 분산을 제곱근으로 줄인 것
##### 추정에 있어 통계학의 손실함수에는 평균제곱오차 또는 음의 로그 우도함수가 있으며
   머신러닝에서도 동일한 손실함수를 사용한다.
##### 우도함수: 우도 함수(가능도 함수로 번역되기도 하고, 영어로는 likelihood function 이라 합니다)
는 실현된 데이터(혹은 관찰된 데이터 observed data)로 부터
특정 통계 모델의 적합성을 확인하는데 주로 이용됩니다.
##### 손실함수 혹은 비용함수(cost function)는 같은 용어로 통계학, 경제학 등에서 널리 쓰이는 함수로
    머신러닝에서도 손실함수는 예측값과 실제값에 대한 오차를 줄이는 데 사용된다.

---
# 4. Master Algorithm

| Tribe                 | Origins              | Master Algorithm              |
|-----------------------|----------------------|-------------------------------|
| Symbolist(기호주의자)      | Logic, Philosophy    | Inverse Deduction(역연역법)       |
| Connectionists(연결주의자) | Neuroscience(인공지능)   | Backpropagation(역전파)          |
| Bayesians(통계주의자)      | Statistics           | Probabilistic Inference(확률추론) |
| Analogizers(분석철학)     | Psychology(심리학)      | Kernal Machines(SVM)      |
| Evolutionaries        | Evolutionary Biology | Genetic Programming           |

### 1) Symbolist(기호주의자)

##### (1) 역연역
### 2) Connectionists(연결주의자)
### 3) Bayesians(통계주의자)

- 베이지 정리 → MCMC(bysian을 해야 이해하기 수월하다)
### 4) Analogizers(분석철학)

---
# 5. 학습
> 신경망으로 테크를 탄 경우 지도, 비지도, 강화' 세 가지로 나뉜다

학습은 통계학에서 추정 문제를 해결하는 과정(=추론)이다
- 지도 학습은 샘플을 사용, 비지도는 샘플을 사용 x
- 지도학습은 분류(classification)와 회귀(regress)로 나뉜다
  > 결국 learning =  target을 구하는 modeling이다
  >
  > model은 var를 잡아내서 class(객체)를 시도한다
- 변수는 feature 와 target 으로 나뉜다.
- 상수는 계수와 편향로 나뉜다.
  - 따라서 다음과 같은 식의 구조를 같는다.
  target(예측값, Hat) = 계수 * feature-value + 편향
  특성변수 = 독립변수 = 외생변수 = x변수
  목적변수 = 종속변수 = 내생변수 = y변수
  - 기대값 y는 다시 y와 y Hat(가설)으로 나눠진다
  feature 의 변환은 표준화와 정규화가 있다.
  아웃라이어가 있으면 표준화 나머지는 정규화가 낫다.
  - 계수(係數, coefficient)는 '인자(因子)'라는 뜻으로 쓰인다.
  - 보통 식 앞에 곱해지는 상수를 말한다.
  - 가장 흔한 계수의 개념은 다항식에서 x n 앞에 붙는 수이다.
  학습은 통계학에서  추정문제 해결과정(=추론)이다.
  learning 은 target 을 구하는 modeling 이다.
### 1) 분류
##### 베르누이(홀짝)
- 베르누이 확률 변수 = x(대문자면 여러개)
- 베르누이 시행 : 호출
### 2) 회귀

### 분포
> 분포는 함수다
>> 확률 질량 함수(PMF) : 리턴값이 정수
>
>> 확률 밀도 함수(PDF) : 리턴값이 실수
- dense는 신경망에서 사용한다
> 확률분포는
>> 이산 - 확률질량함수 PMF: 이항분포, 다항분포, 이산균등분포, 푸아송분포, 베르누이분포, (초)기하분포
>
>> 연속 - 확률밀도함수 PDF: 정규분포(=가우스분포), 연속균등분포, 카이제곱분포, 감마분포
''' 강사님 필기 (추후 병합 필요)## 분포
이산확률변수가 따르는 확률분포인 이산확률분포 중,
대표적인 분포인 베르누이분포(Bernoulli Distribution)와 이항분포(Binomial Distribution)에
시행의 결과가 성공이면 1의 값을 갖고, 실패이면 0의 값을 갖는 확률변수 X를
베르누이(Bernoulli) 확률변수라고 하고, 그 분포를 베르누이 분포라고 합니다.
그리고 이렇게 두 가지의 결과만을 갖는 시행을 베르누이 시행이라고 합니다.
성공일 확률은 p, 실패일 확률은 1-p = q가 되겠습니다.
만약 베르누이 시행을 여러 번 하면 어떻게 될까요?
예를 들어 동전 던지기도, 한번만 하고 끝내는 것이 아니라 5번을 던져서 그중 성공(앞면이라고 가정하죠)이 3번 나올 확률을 계산해볼 수도 있지 않을까요?
이때 사용하는 확률분포를 이항분포라고 합니다.
ㅇ 베르누이분포 : X ~ B(1,p)      (1번 만의 베르누이 시행의 성공 확률분포)
ㅇ 이항분포     : X ~ B(n,p)      (n번 베르누이 시행의 성공 확률분포) 
타깃(y)==함수(f(x))==확률(p)
y와 f(x)는 상태가 다르다
확률은 상태를 가진 함수다

'''
### 무상태 프로그래밍 (RESTful)
> 보안은 우리가 판단하지 말고 그냥 다 무상태로 가라
> <a style=color:red>세션 유지는 내부망 외에는 절대 안돼</a>
> <a href="https://www.postman.com/">포스트맨</a>을 사용해 해당 방식을 제대로 적용했는지 확인이 가능하다
<a href="https://okdone.tistory.com/158">참고 링크</a>
- string으로 보내면 상수값으로서 계속 남아있지만 
- 작성은 딕셔너리 구조를 response에 담아서 보낸다

##### 전제
- 객체지향의 구성 요소는 타입과 객체 참조 그리고 행위이다. 속성은 객체지향의 핵심 구성 요소가 아니다.
  - 
- 속성이 상태를 만든다.
- 이상적인 객체 세계는 무상태이다.
- 상태는 객체 세계와 외부 세계간의 소통을 위해서만 발생한다.
  - 객체세계(장고)/외부세계(리액트)/ 소통(네트워크)
속성=상태에서 여러개였던 상태가 함수를 통해 하나의 타깃값을 갖게되면 상태 하나 밖에 없어서 선택할 수 없는 무상태가 된다
속성을 만들지 않는게 좋다 = 
  - 
## 소스 / 리소스
- 가공 전인 리소스를 가공 후인 소스로 바꿔주는 텍스트 파일이 소스코드
- src 내부의 파일은 소스(여기가 우리의 본진)
- 나머지는 리소스
---
## 도구, 시스템, 서버
- IDE(개발환경) : 도구+언어 
- 도구(또는 시스템) → 개발 환경을 구축하는 시스템, 언어에 의존해서 시스템을 개발(배포 후에는 사라진다)<br/>
- 서버 → 클라이언트의 요청에 의해 서비스를 제공하는 시스템. 즉, 서버와 클라이언트는 상황에 따라 달라진다<br/>
- 시스템 → 개발 환경을 통해 구축한 서버와 클라이언트 → 결국 서버와 클라이언트의 본질<br/>

    > 서버인지 클라이언트인지는 결국 역할에 따라 달라진다

> 프로젝트를 진행한다 = 도구와 언어를 이용해 시스템을 만드는 것<br/>

- request와 response는 본질은 같지만 방향만 다르다 (동시에 한 공간에 있을 수 없다)

---
## 관계
#### is a
> 상관 관계
#### has a
##### 연관 관계(생명 주기가 동일)
    > 상속 등
##### 의존 관계(생명 주기가 다르다)

---
## 단방향 / 양방향
<a href="https://jeong-pro.tistory.com/231"> 참고 </a>
- 개념을 잊어서 사고치지말자
- 프론트에서 단방향은 절대 자식에서 부모로 올라갈 수 없다

---
## 라이브러리와 프레임워크의 차이
- 라이브러리와 프레임워크 간에 포함관계는 없다
- 장고, 플라스크는 시작부터 프레임워크, 리액트는 둘 다 가능
- 라이브러리
  - 모듈과 패키지의 집합
    - 패키지(컴파일언어) - (인터프리터 언어는 디렉토리 사용-> 프로젝트는 디렉토리를 사용)
      - 모듈들을 하나의 상위 폴더에 있다
      - 패키지 안에 여러가지 폴더가 있을 수 있다
    - 모듈 : 재사용이 가능한 클래스의 집합
- 프레임워크
  - 작업의 구조가 정해진 라이브러리 → 제어흐름을 갖는 시스템
  특정 문제 해결을 위해 상호 협력하는 클래스와 인터페이스의 집합으로 프로그래머의 작업이 필요
> 차이점
> - 코드의 <a style=color:rgb(178,102,255)>제어 흐름</a>
>   - 흐름이 사용자에게 있으면 라이브러리, 시스템에게 있으면 프레임워크
>   - 라이브러리는 사용자가 객체나 함수를 <a style=color:red>직접 호출</a>
>   - 프레임워크는 프레임워크에 의해 메서드가 호출<p>
>>  제어흐름 : 프로그램에서 실행되는 함수가 <a style=color:rgb(178,102,255)> 호출되는 순서</a>

> 프레임워크는 충분조건, 라이브러리는 필요조건(1:1이면 필요충분조건)

> 둘의 구분은 개발자의 손을 탔는지가 아니라 

명칭 그대로 도서관에서 필요한 파일(패키지)과 문서(모듈)를 꺼내서 다른 곳에 옮겨적는 것처럼 사용자에게 제어 흐름이 있고
프레임워크는 건축의 뼈대처럼 정해진 틀 안에서 작업을 수행해야하기 때문에 프레임워크에게 제어 흐름이 있다?

## prefix(접두사) / postfix

## 인조키
- 시퀀스
- uuid

---
## 이미지 / 컨테이너
- 이미지 : 특정 프로세스를 실행하기 위한 모든 파일과 속성값 
## 상태(state)값과 설정(context)값(-it)
- 상태 : 변하냐 변하지 않냐의 차이
  - 변하는 상태는 상태값, 변하지 않는 상태는 설정값
  - 파라미터와 아규먼트는 각각 설정값과 상태값 중 뭘 가지나?
- 파이썬 입장에서 이미지는 class, 컨테이너는 인스턴스, 도커는 파일, 디렉토리는 설정값, 패키지는 상태값
- 설정값 오류가 났을 때는 rm 후 도커파일의 설정값을 다시 설정한다. 
- 메인영역의 메타데이터는 변경이 없지만 서브 영역은 상태가 변한다
> ※ 설정값은 상수가 아님을 기억해라
---
## 컴포넌트와 컨테이너
- 컴포넌트 : 재사용이 가능한 객체
- 컨테이너 : 여러 컴포넌트를 담는 객체
---

## Atomic Pattern
- Atom → Molecule → Organism → Template → Page
    > 기본적으로 하위 개념은 상위 개념의 컴포넌트고 상위 개념은 하위 개념의 컨테이너
    >> 여기서는 원자, 분자, 유기체를 컴포넌트, 템플릿을 컨테이너로
    
#### Atom
- 가장 작은 단위의 컴포넌트
- 어떤 설정값이 주어져도 생성되어야해서 다양한 상태값을 가지고 있어야한다
- 마진이나 위치값을 가지지 않는다
 
---
## work, job, task

---
## MSA
## EDA(이벤트 드리븐 아키텍처)
> 이벤트 주도 : 체인 메소드

## 이벤트 버블링 캡쳐링
> 버블링 : 자식에서 부모로 이벤트가 전딜
> 캡쳐링 : 부모에서 자식으로 이벤트가 전달
<a href="https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/"></a>
- 람다로 하면
  
  
    const onClick = e=>{}

- 에러시 consol.lig로 버블이 끊긴 부분을 해결해야한다
<a style="color:p">버블링과 캡쳐링은 느리다 스토어에 집어넣는 디스패치를 이용해서 사용</a>

#### <a style="color:red">한 컨테이너에 양, 단방향을 둘 다 넣지마라</a>

---

## 크로스 플랫폼(브릿지패턴)
## 덕 타이핑(덕 패턴)
> 객체의 타입이 아닌 메소드의 역할에 의해 객체의 역할이 주어지는 형태
> 객체(클래스) 기반이 아니라 함수지향 - 함수를 통해
#### 기존의 리덕스
- action, store(actiontypes), reducer를 필요조건으로 가진다(세 개 동시면 충분조건)
#### 덕 타이핑을 하면
- components, container, store로 돼있던(12-05) 모듈들을 각 컨텐츠인 todos, counter등으로 나눈다(12-06)

---
## stateful/ stateless

---
# Router (ERD의 Cross Entity와 같은 개념)

데이터프레임  csv 

on_delete 부모가 지워지면 같이
CASCADE

바닐라js
리액트 : 바닐라js에 라이브러리를 올린 것

## 클라이언트 서버

## json
1. json의 구조 
   - 파이썬 딕셔너리({})나 리스트([], json에서는 array)구조와 동일하다
- 

## 서버
#### 서버 객체 생성
    listen(port, [hostname], [backlog], [callback])

---
- 방법
  - 생성자 a=A()구조
  - 팩토리 pd.~구조

- a = b에서 값인 b가 설정값과 상태값이다  
  - 상태값 : 불규칙하고 바뀐다
  - 설정값(context) : 맥락이 있다 
  - 전역에 들어가면 거의 설정값, 지역은 상태를 갖는다
  

| --- |클라이언트 서버 | 웹서버 | was | db 서버|
|-----|---|---|---|---|
|  언어 |리액트|---|---|sql|


### CORS
- sgi.py는 공유기 같은 역할 백에서 받은 내용을 프론트로 보내주는 역할
- 크로스 관계는 두 객체가 서로 만나지 않고 기능을 공유한다.
---
tip?
과정이 필요한 이유를 이해해야지 그냥 외우는 공부는 x

## JavaScript 
- ES(ECMAScript)6이상을 공부해야 인공지능에 사용 가능
- 스크립트 -> 인터프리트 언어(컴파일 후 실행되는 컴파일과 달리 인터프리터는 바로 실행되기 때문에 더 어렵다)

## React
- SPA(single-page application)나 모바일 애플리케이션 개발에 사용 가능
- 규모가 커지면 라우팅(WSGI), API통신 등이 요구
- 라우팅과 API통신은 크로스(ERD의 크로스 엔티티와 같은 개념)
## 
인공지능 베이스에서는 뷰보다 리액트
안드로이드에서는 뷰가 더 좋다


---

## SPA(Single Page Application)와 MPA(Multiple Page Application)
- MPA였을 때는 페이지 별로 코딩을 했지만 SPA를 사용하면 메모리 절약으로 인한 속도 향상이 가능
  - 페이지 요청시마다 정적 리소스를 다운로드는 MPA와 달리 SPA는 모든 정적 리소스를 최초 한 번에 다운로드한다
- 이미 정해진 코딩이 있는 MPA방식은 사용자에 따라 달라져야하는 인공지능에 부적합하고 속도도 느려서 SPA를 사용

## 파이썬 구조분산 할당

# SPA
> 메모리 상에는 하나의 페이지만 존재한다(html은 여러개여도 된다)

# pub sub 패턴
- event data store 부분이 우리가 코딩하는 부분

##### store의 의미
- pub-sub에서 event data store
- 화면처리에서는 컨테이너를 사용하고 스토어에는 데이터만 존재하도록 나눈다 
- 상태 전부가 담기는 충분조건

상대적인 개념이지만 설정의 위치에 있는 것들은 const(함수)로 나온다

#### <div style=color:red>★★★★★ 이제 동기식이 아니라 비동기식으로 개발해야한다<p/>

---
## 맵 필터 리듀스

--- 
## Redux
- 예측 가능한(=충분조건) 상태 컨테이너
  - = 충분조건이 만족되면 자동으로 작동하는 컨테이너
- 스칼라(단일값)으로 
---
#### 리액트 생태계는 프레임워크지만 리액트 안은 라이브러리

##### 필요 충분 조건
- 필요조건 : 반드시 필요한 조건(val)
- 충분조건 : 만족되면 진술이 참인 조건(var)
> var = val

## 상태와 상태값
- 상태 : 컨테이너 내부의 빈 공간
- 상태값 : 
- 차이 : 
<a href ="https://zdnet.co.kr/view/?no=20221202183934">이벤트 드리븐</a>
## axios
> react와 django를 연동할 때 사용
## 이미지 처리

---
12-06
## MSA
> 비동기식 연습
> 
## {...input, [name] : value }의 의미
<img src="C:\Users\AIA\Downloads\5.png">
dispatch:외부에서 입력받은 객체인 action을 store로 보내주는 역할
store:view인 쟝고로 보낸다
- dispatch에 담기면 store에 담기기 전에 빠져나갈 수 없다

dispatch(addTodo({text:value}))에서
함수 부분인 addTodo({text:value})가 action이다
 
const todoSlice = createSlice({
  name: 'todos',
  initialState: [],

---
장고 연결
---

## 데이터
- Data (info와의 차이는 )
- DB : 데이터 저장소 (스토리지와의 차이는 디스크/메모리)
- DB Tool
- DBMS
- DB Server
- DB Center
- Data Warehouse
- Data Set

batch : 샘플을 자른 것

## Ground Truth
> 실제값
> 
> ### 데이터셋
지금까지 데이터는 train set과 test set 두개로만 나누었지만 train, test 두개로만 분리하는 것은 기초적인 수준, 
보통 현업에서 모델(커스텀모델)을 만들 때는 아래 세 개로 나눈다
- train → 기출
- test(=Unseen data, 학습과 검증이 끝난 모델의 최종 성능 평가용) → 수능
- validation set(학습이 완료된 모델을 검증하기 위한 set(중간점검용)) → 모의고사
  - 수시로 사용해야 되므로 Cross validation을 사용한다


validation dataset is a sample of data held back from training your model that is used to give an estimate of model skill while tuning model’s hyperparameters.
The validation dataset is different from the test dataset that is also held back from the training of the model, but is instead used to give an unbiased estimate of the skill of the final tuned model when comparing or selecting between final models.
There is much confusion in applied machine learning about what a validation dataset is exactly and how it differs from a test dataset.

### criterion 은 표준이다. 동의어로는
standard, normal, norm, average, level 이 있다.

### 엔트로피(영어: entropy, 독일어: entropie):https://ko.wikipedia.org/wiki/%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BC
열역학적 계의 유용하지 않은 (일로 변환할 수 없는) 에너지의 흐름을 설명할 때 이용되는 상태 함수다.
통계역학적으로, 주어진 거시적 상태에 대응하는 미시적 상태의 수의 로그로 생각할 수 있다.
엔트로피는 일반적으로 보존되지 않고, 열역학 제2법칙에 따라 시간에 따라 증가한다.
독일의 물리학자 루돌프 클라우지우스가 1850년대 초에 도입하였다.
대개 기호로 라틴 대문자 S를 쓴다.


## 불순도(gini)
### DecisionTree Learning 에서 불순도를 계산하는 3가지 방법
https://m.blog.naver.com/samsjang/220978650404
지니 인덱스
엔트로피
분류오류

### 불순도란 다양한 범주들의 개체들이 얼마나 포함되었는가 정도이다.
여러가지 클래스가 섞여있는 정도이다. 반대로 순수도(purity)는 같은 클래스끼리
얼마나 많이 포함되어 있는지를 말한다.
https://computer-science-student.tistory.com/60

## 객체 모델(Object Model)

### criterion
> = 표준

## CCEE(Categorical Cross Entropy Error)

### Entropy
> 사전적인 정의 : 함수 / 통계적 의미 : 기대값

### 지니계수

### Decision tree
random forest 알고리즘의 기본이 되는 알고리즘으로 tree 기반 알고리즘

### 하이퍼파라미터
model : D에서 
d = D(파라미터)  
d.hook() 일 때 hook이 생략된 D의 파라미터를 받는 것

### Random Forest
> 앙상블 학습의 대표


## 가설 (Hypothesis)
t-value (타깃값) : 둘로 나뉜다
p-value (확률값) : 타깃값의 확률
귀무 가설(null hypothesis)이 맞다는 전제 하에,
표본에서 실제로 관측된 통계치와 '같거나 더 극단적인' 통계치가 관측될 확률이다.

> #### 귀무 가설(歸無假說, 영어: null hypothesis, 기호 H0) 또는 영 가설(零假說)
> 통계학에서 처음부터 버릴 것을 예상하는 가설이다.
> 차이가 없거나 의미있는 차이가 없는 경우의 가설이며
> 이것이 맞거나 맞지 않다는 통계학적 증거를 통해 증명하려는 가설이다.
> 예를 들어 범죄 사건에서 용의자가 있을 때
> 형사는 이 용의자가 범죄를 저질렀다는 추정인 대립가설을 세우게 된다.
> 이때 귀무가설은 용의자는 무죄라는 가설이다.
> 통계적인 방법으로 가설검정(hypothesis test)을 시도할 때 쓰인다.
> 로널드 피셔가 1966년에 정의하였다

기술 통계 -(가설)→ 추론통계 = 학습(learning)
가설로부터 추론을 이끌어내는게 머신러닝


## 알고리즘, 함수, 모델 차이
알고리즘(process) : 스레드(러닝중인 메소드)의 집합 : hook 
로직(if, for) 
함수 : def(밖에 있으면 함수, 안에 있으면 method)
모델 : class

## 함수와 식의 차이
y = ax + b인 식은 즉시 실행돼서 통제가 불가능
f(x)인 함수에서는 필요한 지점에서 사용 가능



## 산술급수/ 기하급수


##
fit_transform()은 train dataset에서만 사용됩니다
transform()은 test data에 적용하기 위해 를 사용한다.

## 행렬 연산(Matrix Operations)

 행렬 표기법 - Matrix Notation

 행렬 덧셈 - Matrix Sum
 스칼라 곱 - Scalar Multiple
 행렬 곱 - Matrix Multiplication
 행렬의 전치 - The transpose of a matrix

## 선형회귀
diff: 로지스틱회귀

---
### 그냥
- ~법은 메소드, ~기능은 함수로 해석해라
- 절차가 있는 메소드는 hook, ML에서의 모델은 클래스(이후에는 파일로도)



---
# 위치정리 필요
## 베르누이 시행(=이진분류)
## 로지스틱 회귀(시그모이드 함수)
<a href = "https://datascienceschool.net/03%20machine%20learning/10.01%20%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1%20%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.html"> 링크 </a>
- 판별함수 : z(표준) = u(평균)인 함수
- 종속변수가 이항분포에 따르고 그 모수(데이터셋)가 독립변수(샘플)에 의존한다
  - 모수는 독립변수(x)들의 집합이니까
