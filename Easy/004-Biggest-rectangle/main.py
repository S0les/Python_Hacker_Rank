def brute_force(heights):
    max_area = 0

    for i in range(len(heights)):   # Переменная принимает значение списка
        min_height = heights[i]     # Присваиваем переменной значение в зависимости от индекса i из списка heights
        for j in range(i, len(heights)):    # От значения i до одного из значений списка
            min_height = min(min_height, heights[j])    # Возращаем меньшее из 2
            curr_area = (j - i + 1) * min_height    # Считаем Область
            max_area = max(curr_area, max_area)     # Возращаем большее из 2

    return max_area     # Возращаем как значение функции переменную max_area


hist = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    hist.append(ele)
print(brute_force(hist))
