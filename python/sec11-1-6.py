sizelist = ["XS", "S", "M", "L"]
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = lambda item : sizelist.index(item))
print(data)
