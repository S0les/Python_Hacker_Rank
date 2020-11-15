user = (input('your list: '))   # Берет значения для списка
lis = user.split()      # Отделяет значения (по пробелу) и переобразовывает в список
result = [int(item) for item in lis]    # Конвертируем из str в int
result.sort()      # Сортирует по возрастанию
if len(result) > 1:     # Убираем вариант если 1 число в последовательности
    d = (max(result)-min(result))/(len(result)-1)      # Шаг
    if d == int(d):     # Проверка целый ли шаг
        print(True)
    else:
        print(False)
else:
    print(False)
