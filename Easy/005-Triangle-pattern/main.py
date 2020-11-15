hei = int(input("height: "))
amount = int(input("amount: "))
for height in range(1, amount+1):      # Колово триугольников
    for long in range(1, height+hei):  # Высота
        for i in range(1, long+1):     # Длина строки
            print("*", end=" ")    # Значение строки
        print()     # Переход между строками
