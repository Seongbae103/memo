# 회문 판별과 N-gram 생성
## 1. 회문
- 회문?
> 앞, 뒤 어느 순서로 읽어도 같은 단어나 문장
> - 예 : 기러기 토마토 스위스 인도인 별똥별 우영우

### 1.1 반복문으로 회문 검사
    txt = input('단어 : ')
     
    is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
    for i in range(len(txt) // 2):      # 0부터 문자열 길이의 절반만큼 반복
        if txt[i] != txt[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            is_palindrome = False        # 회문이 아님
            break
     
    print(is_palindrome)                 # 회문 판별값 출력

### 1.2 시퀀스 뒤집기로 검사
    txt = input('단어를 입력하세요: ')
     
    print(txt == txt[::-1]) 

### 1.3 리스트와 reversed 사용
    txt = input('단어를 입력 : ')
    list(txt) == list(reversed(txt))

### 1.4 join과 reversed 사용
    txt = input('단어를 입력 : ')
    txt == ''.join(reversed(txt)

## 2. N-gram 만들기
N-gram?
> 문자열에서 연속되는 n개의 요소를 추출하는 방법

### 2.1 반복문으로 N-gram
    # 글자 단위인 경우
    txt = input()
    for i in range(len(txt) -1):  #2-gram이면 뒤에서 두 번째까지만 반복되니까
        print(txt[i], txt[i+1], sep='')
    # 단어 단위인 경우
    txt = input()
    words = text.split()
    for i in range(len(words) - 1):  
        print(words[i], words[i + 1])
### 2.2 zip으로 N-gram
    text = 'hello'
     
    two_gram = zip(text, text[1:])
    for i in two_gram:
        print(i[0], i[1], sep='')

### 2.3 zip과 리스트 표현식으로 N-gram
    text = 'hello'
    [text[i:] for i in range(3)]