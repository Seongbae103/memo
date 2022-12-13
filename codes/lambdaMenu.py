IRIS_MENUS = ["종료", #0
            "데이터구조파악",
            "전체 실행"]

iris_menu = {
    "1" : lambda t : t.spec(),
    "9" : lambda t : t.hook()
}

if __name__ == '__main__':

    t = Iris()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == 0:
            print("종료")
            break
        else:
            iris_menu[menu](t)
