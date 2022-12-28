# PyCharm
### 1. <a href="https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows">파이참 설치</a>
※ Create Associations, Update PATH variable(restart needed)는 필수 체크(전체 체크 권장)
### 2. 설정
- 첫 설치시 'Do not import settings'선택
- env
  - Configs → Settings → Project interpreter → System Interpreter → Python.exe경로 설정
- venv
  - PyCharm-> Preferences -> Project -> Python Interpreter -> 인터프린터 선택 중 Show All → add(+)

### 3. 터미널에 venv 자동으로
- tool - terminal - shell path에서 디폴트를 cmd로
### 4. venv 에러
> case1
>> 2022.2.3 버전의 경우 버전 이슈가 있다 삭제 후 2022.2.2 버전으로 다시 설치
>
5. 터미널에서 가상환경 사용
- venv 경로로 들어가서  .\Scripts\Activate.ps1 
