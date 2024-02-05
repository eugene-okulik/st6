# Задание №2
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 != 0):
        print("fuzz")
    elif (i % 5 == 0) and (i % 3 != 0):
        print("buzz")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("FuzzBuzz")
    else:
        print(i)
