# 머신러닝
★☆★☆설치시 중요 base★☆★☆

 

conda create -n scalar anaconda python=3.8

conda activate scalar

conda list

conda info -e # 가상환경 정보보기 명령어

conda update --all
### 드라이버 설치
> 현재 텐서플로우 파이토치 공식 홈페이지에서 말하는 필요한 cuda와 cudnn의 버전은 윈도우 10까지의 버전인
해당 버전들까지만 지원

- windows + puase 그래픽카드 확인
- 버전에 맞는 드라이버 설치 <a href =" https://www.nvidia.co.kr/Download/index.aspx?lang=kr#">참고</a>
### CUDA 설치
<a style=color:red> 설치 순서는 드라이버 -> 쿠다 - cudnn</a><br/>
<a href="https://developer.nvidia.com/cuda-11.2.0-download-archive?">설치 링크</a>

- target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

### cudnn설치
- 터미널의 cd C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include에서<br/>
notepad chdnn_version.h로 버전 확인(아래 코드에서는 8.4.0)


     #define CUDNN_MAJOR 8
     #define CUDNN_MINOR 4
     #define CUDNN_PATCHLEVEL 0
- 버전에 맞는 cunn설치
- cudnn/cuda 경로에서 bin. lip, include를 <a style=color:red>C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2</a>로 옮긴다→ 
- bin. lip, include의 환경변수를 설정한다(아래 환경변수 항목을 참고)

## TensorFlow
conda create -n [환경이름할꺼] python=3.8

-전역에 설치 시 충돌이 날 수 있어서 무조건 conda activate [본인환경이름]을 치고 시작하세요!!!

### ★☆★☆콘다 명령어 모음(순서대로)★☆★☆
<a style=color:red>아나콘다 프롬프트로 깔아야 한다!!</a>(버젼 바로 설치 시 오류 가능성 있다)

pip install tensorflow==2.9.1 ## 텐서 안쓰면 설치안해도됨
pip install tensorflow-gpu==2.9.3 ## 텐서 안쓰면 설치안해도됨
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
pip install transformers==4.8.2
pip install sentencepiece==0.1.91
pip install torchsummary
conda install -c conda-forge icecream
pip install mysql-connector-python
pip install flask
pip install konlpy==0.5.2
pip install pandas
pip install scikit-learn
pip install jupyter
pip install opencv-python

---
## 환경변수
ANACONDA_HOME1
C:\ProgramData\Anaconda3
ANACONDA_HOME2
C:\ProgramData\Anaconda3\Scripts
ANACONDA_HOME3
C:\ProgramData\Anaconda3\Library\bin
ANACONDA_HOME4
C:\ProgramData\Anaconda3\Library\mingw-w64\bin

JAVA_HOME
C:\Program Files\jdk-11

NODE_HOME
C:\Program Files\nodejs

<★path★>
C:\Program Files\jdk-11\bin
C:\ProgramData\Anaconda3
C:\ProgramData\Anaconda3\Scripts
C:\ProgramData\Anaconda3\Library\bin
C:\ProgramData\Anaconda3\Library\mingw-w64\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\lib

---
## Errors
#### SDK가 이미 있다는 알림
> FrameView SDK를 지우고와서 쿠다 설치 다시 시도
#### 확인
import torch
import tensorflow as tf
import sklearn

print(f"토치 버전 : {torch.__version__}")
print(f"텐서플로 버전 : {tf.__version__}")
print(f"사이킷런 버전 : {sklearn.__version__}")
print(f"torch의 gpu 사용 가능 여부 확인 : {torch.cuda.is_available()}")
print(f"사용가능한 gpu 보기 : {torch.cuda.get_device_name(0)}")
#### gpu 사용 false시
conda uninstall pytorch
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
