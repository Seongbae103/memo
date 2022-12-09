OKLAHOMA_MENUS = ["종료", #0
                "데이터구조파악",#1
                "변수한글화",#2
                "연속형변수편집",#3 18세이상만 사용함
                "범주형변수편집",#4
                "샘플링",#5
                "모델링",#6
                "학습",#7
                "예측"]#8

oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.categorical_variables(),
    "5" : lambda t: t.sampling(),
    "6" : lambda t: print(" ** No Function ** "),
    "7" : lambda t: print(" ** No Function ** "),
    "8" : lambda t: print(" ** No Function ** "),

}
def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Oklahoma() #모델명()
    while True:
        menu = my_menu(OKLAHOMA_MENUS) #(메뉴 목록)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                oklahoma_menu[menu](t) #실행메뉴명[menu](t)
            except KeyError:
                print(" ### Error ### ")
