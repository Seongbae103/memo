# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
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

### 2.3 pormise
> subscribe, 옵저버 패턴
- 종류
  - axios : 양방향
  - fetch : 단방향
  > react는 단방향 데이터 흐름을 처리하기 때문에 우리 코드에서는 fetch를 사용했다


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

## Redux
> 리액트에서 사용하는 라이브러리로 컴포넌트 상태의 업데이트 관련 로직을 다른 파일로 분리시켜서 관리 가능
#### redux 용어
- 액션 
  > 상태의 변화가 필요할 때 사용
- 액션 생성함수
  > 액션 객체를 만들어주는 함수, 화살표 함수로도 표현 가능
- 리듀서
  > 현재 상태와 액션 객체를 받아서 새로운 상태를 리턴하는 함수
- 스토어
  > 상태가 들어가며 하나의 프로젝트는 하나의 스토어만 가질 수 있다
  - 디스패치
    > 스토어의 내장함수 중 하나로 액션 객체를 넘겨줘서 상태를 업데이트 하는 유일한 방법
    > 

<a href ="https://kyun2da.dev/%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC/Redux-%EC%A0%95%EB%A6%AC/">redux 참고한 블로그</a>

    import webcrawler from "../api"
    import {useState} from 'react'
    const NaverMovie = ()=> {
        const [movie, setMovie] = useState()
        const onClick = e =>{
            e.preventDefault()
            webcrawler.getNaverMovie().then(res => {
                const json = JSON.parse(res)
                setMovie(json['result'])
            })
            let arr = document.getElementsByClassName('box')
            for(let i=0; i<arr.length; i++) arr[i].value = ""
        }

        return (<>
        <h5>네이버 크롤러</h5>
        <button onClick={onClick}>크롤링 시작</button>
        <p>버튼을 클릭하면 네이버 영화 목록이 출력</p>
        <table>
            <thead>
                <tr>
                    <th>순위</th><th>영화 목록</th>
                </tr>
            </thead>
            <tbody>
            {movie && movie.map(({rank, title})=>(
                <tr key={rank}><td>{rank}</td><td>{title}</td></tr>
            ))}    
            </tbody>
        </table>     
        </>)
    }
    export default NaverMovie
에서 
