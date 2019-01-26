numbers = [2.1, 4, "", 2.2, "1", 3]
numbers = [num for num in numbers if isinstance(num, (int, float))]
print(numbers)
