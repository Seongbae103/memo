# React
### node_module은 설정값이라 무거우니까 주의
## 설정 
> 순서 : vscode → node → npm → yarn
### 1. vs코드 설치
### 2. 언어팩 설치(인공지능에 사용할거라면 ES6 이상으로)
> - 도커, js, 리액트 팩 설치   
### 3. <a href ="https://nodejs.org/ko/download/">node 설치</a>해서 노드로 소스코드 이용
> node.js의 패키지 관리자로 npm이 기본으로 설치된다 (인공지능을 원하면 yarn을 쓴다)
### 4. npm으로 <a href="https://yarnpkg.com/package/react">yarn설치</a> → yarn으로 리액트 설치
오피셜로 설치해도 좋지만 아래처럼 쓰는게 더 편하다<p>
※ 실체는 분산되더라도 동일한 터미널로 묶여있어야 작동한다 

    npm install yarn -g 

yarn list에 아무것도 없으면 CRA사용 

    yarn create react-app <프로젝트명>
### 사용
cd로 경로에 들어가서 

    yarn start
- src에서 코딩
  - index.js의 <App />는 App.js
---
### error
#### case.1 
> <p style=color:red>npm : The term 'npm' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again. At line:1 char:1</p>

> 해결 : <p>
> - Terminal을 관리자 권한으로 오픈한 뒤 Set-ExecutionPolicy Unrestricted 를 입력<div>
> - vs코드를 껐다 켠 뒤 터미널에 yarn 입력해서 확인

---

