id_list = ["a2345", "a1236", "b7656", "0987"]
while True :
    id = input("idを入力してください:")
    if id == "q" :
        print("終了しました")
        break

    try :
        pos = id_list.index(id)
        print(str(pos + 1) + "番目のメンバです")
    except :
        print("メンバではありません")


        