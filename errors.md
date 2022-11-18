### error: (-215:Assertion failed) !empty() in function
> 원인
>>- haarcascade_fronface.xml이 프로젝트 파일에 없을 때
>>- 경로가 잘못됨

> 해결
>> 두 번째의 경우 *params 순서가 잘못됨(아래 코드로 확인) 
> 
    if param.size == 0:
    print("### param is null ### ")
    else :
    print(" ### param is not null ### ")

### 
> 원인
>>- df에 int와 str이 섞여서

> 해결
>>  regex 사용 <p> (self.seoul_crime[cols].str.replace(',', '')을 쓰는 방법도 있지만 불필요한 루프가 생겨서 효율x)
> 
    self.seoul_crime = pd.read_csv('./data/crime_in_seoul.csv')
    cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
    self.seoul_crime[cols] = self.seoul_crime[cols].replace(',', '', regex=True).astype(int)
참고한 내용 : <a href>https://acdongpgm.tistory.com/166

### TypeError: 'NoneType' object does not support item assignment
> 문제
>>
> 원인
>>- 

> 해결
>>  
> 
    code