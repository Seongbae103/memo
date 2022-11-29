# Anaconda3
### 1. <a href="https://www.anaconda.com/products/distribution#download-section">아나콘다 설치</a>
<div> ※ CUDA를 사용해야 할 경우 All Users를 체크하지만 작업 장소의 정책에 따라 달라진다</div>
<p>- 경로 : c:\ProgramData\Anaconda3</p>
<div>- Register Anaconda as my default Python 3.(버전) 체크</div>

### 2. 환경변수 설정
- sysdm.cpl ,3
- 아나콘다 환경변수 설정값
    > ANACONDA_HOME1(변수명)
    >> C:\ProgramData\Anaconda3(변수값)

    > ANACONDA_HOME2
    >> C:\ProgramData\Anaconda3\Scripts

    > ANACONDA_HOME3
    >> C:\\ProgramData\Anaconda3\Library\bin

    > ANACONDA_HOME4
    >> C:\ProgramData\Anaconda3\Library\mingw-w64\bin
- 시스템 변수에 입력 후 path에 '%변수명%'으로 추가
- cmd창에서 버전 확인
    > conda --version
