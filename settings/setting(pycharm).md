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
> setting - Tool - terminal shell path에
> - 'powershell -NoExit -File ".\venv\Scripts\activate.ps1"
>> 에러 발생시 power shell 관리자 권한으로 실행 후 "Set-ExecutionPolicy Unrestricted"입력

### 4. venv 에러
> case1
>> 2022.2.3 버전의 경우 버전 이슈가 있다 삭제 후 2022.2.2 버전으로 다시 설치
>
