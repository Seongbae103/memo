# scaffold
>  초기 프로젝트의 뼈대를 만들어주는 행위
>> ml에서는 처음 메뉴, df 등을 만드는 순서 
- csv파일이 다수 일 때, self.~하는 것보다 아래처럼 만드는게 더 편하다
    def spec(self, x):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(x.shape)
        print(" --- 2.Features ---")
        print(x.columns)
        print(" --- 3.Info ---")
        print(x.info())
        print(" --- 4.Case Top1 ---")
        print(x.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(x.tail(3))
        print(" --- 6.Describe ---")
        print(x.describe())
        print(" --- 7.Describe All ---")
        print(x.describe(include='all'))
    - 여기에서 'x'는 어떤 값이 들어와도 받는다는 뜻으로 사용