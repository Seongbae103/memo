관리자권한으로 cmd 열기


cd C:\Windows\System32\drivers\etc

notepad hosts

맨아래에 93.184.215.201 download.visualstudio.microsoft.com 붙여넣기.

ALT + F4  저장하기

cmd 닫기

USB 크롬,자바 11, 아나콘다, 쿠다, VS코드,  터미널, 깃 설치

WINDOW키 + r

sysdm.cpl ,3

### 자바 환경변수 1개 등록

JAVA_HOME

C:\Program Files\Java\jdk-11.0.15

JAVA_HOME

### 아나콘다 환경변수 4개 등록

ANACONDA_HOME1
C:\ProgramData\Anaconda3
ANACONDA_HOME2
C:\ProgramData\Anaconda3\Scripts
ANACONDA_HOME3
C:\ProgramData\Anaconda3\Library\bin
ANACONDA_HOME4
C:\ProgramData\Anaconda3\Library\mingw-w64\bin

### 쿠다설치, 환경변수 3개등록

cudnn 속 cuda 폴더에서 bin, include, lib 3개를 

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2 오버라이딩 

CUDA_HOME1

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin

CUDA_HOME2
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include

CUDA_HOME3
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\lib

### path 등록

%JAVA_HOME%\bin

%ANACONDA_HOME1%


%ANACONDA_HOME2%
%ANACONDA_HOME3%
%ANACONDA_HOME4%

%CUDA_HOME1%


%CUDA_HOME2%
%CUDA_HOME3%

### 터미널 열기

java --version 

[출력] 11.0.15

conda -V

[출력] 4.12.0

nvcc -V 

[출력] 11.2

 

cd 'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include'

notepad cudnn_version.h

오픈된 파일 하단부에서 8.1.0 체크.

#define CUDNN_MAJOR 8
#define CUDNN_MINOR 1
#define CUDNN_PATCHLEVEL 0

메모장 닫기.

터미널 닫기.

관리자권한으로 아나콘다 열기.

conda create --prefix=/ProgramData/Anaconda3/envs/scalar python=3.8

conda activate scalar

conda list

conda info -e 

 

단, 설치할 때  privilege 오류 발생하면 권한주기:  python -m pip install -U pip --user

pip install --upgrade pip
pip install tensorflow==2.7.0

pip install tensorflow-gpu==2.7.0

conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge

pip install transformers==4.8.2

pip install sentencepiece==0.1.91

pip install torchsummary

conda install -c conda-forge icecream

pip install konlpy==0.5.2

pip install pandas

pip install scikit-learn

pip install jupyter

pip install opencv-python

 

python

import torch

import tensorflow as tf
from tensorflow.python.client import device_lib

print(' ### 이 PC에 설치된 디바이스 상세보기 : ')
print(device_lib.list_local_devices())

print(' ### 토치버전 :  ')

print(torch.__version__)

print(' ### CUDA 프로그래밍 가능여부 :  ')
torch.cuda.is_available()
device = torch.device('cuda:0' if USE_CUDA else 'cpu')
print(' ### 학습을 진행하는 기기: ',device)

print(' ### CUDA 프로그래밍 가능여부 :  ')

print(torch.cuda.get_device_name())

print(' ### 사용 가능 GPU 갯수 :  ')

print(torch.cuda.device_count())

결과 출력 확인 후 나가기

quit() 

USB 비주얼스튜디오(VS) 설치

워크로드 탭누르고 C++ 데스크톱 개발 체크 후 우측하단 설치 클릭

설치 성공 후 수정 클릭

개별 구성요소 탭 클릭 후 검색창에 14.00 입력

MSVC v 140 체크 후 우측 하단 수정버튼 클릭

다시 다운로드 화면 진행됨

 

pip install mxnet

cd C:\ProgramData\Anaconda3\envs\scalar\Lib\site-packages

start .

numpy 로 시작되는 폴더 3개 삭제

pip install gluonnlp

pip install pytorch_lightning==1.2.10

pip install -I transformers --no-cache-dir --force-reinstall

pip install --upgrade --no-deps --force-reinstall git+https://git@github.com/SKTBrain/KoBERT.git@master

출처 : <a href="https://parksrazor.tistory.com/787"> 여기</a>