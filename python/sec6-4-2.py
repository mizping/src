name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["せいな", "ゆみ", "けいこ", "くんか", "ゆきえ"]
longname = []

for n1, n2 in zip(name1, name2) :
    longname.append(n1+n2)
print(longname)

