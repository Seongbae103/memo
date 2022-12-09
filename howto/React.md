# React 
※ react native는 모바일이다

---
목록
1. 실행
2. 문법 <div>
2.1 람다<p>
2.2 네비게이터<p>
1. 파일별 기능
---
## 1. 실행
cd로 경로에 들어가서 

    yarn start
- src에서 코딩
  - index.js의 <App />는 App.js

## 2. 문법
- index에서 export {default as '.jsx의 파일명'} from '경로'
- "/" : 루트 도메인
### 2.1 람다 사용
(1)


    import logo from './logo.svg';
    import './App.css';
    
    function App() {
      return (
        <></>
      );
    }
    export default App;

(2) function도 생략


    const App = () => {
      return (
        <></>
      );
    }
    export default App

(3) return 없으면 이렇게 축소


    const App = () => <></>
    export default App


const App = () => {}에서
const App은 상수
() => {}은 함수

### 2.2 네비게이터 
> 네비게이션은 상태을 보관할 필요가 없다


---
## 파일별 기능
#### index.js
> 파이썬의 __init__.py처럼 설정값을 상태값으로 지정하는 파일
- 디렉토리를 패키지로 만들어주는 개념

#### src
> 소스코드

#### Container / Component 
> Container 
>> 추상 클래스로
> Component
>> 

## InterFace
> 상속, 인과에는 없고 의존 관계에만 존재