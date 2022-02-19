# Python3.9
# Здесь реализован алгоритм (через 2 функции) сортировки слиянием (merge sort). Я считаю что он оптимален или близок к тому
# за счёт своей быстрой работы О(n log n), а главное стабильной скорости на любом массиве. Выбор был между быстрой сортировкий
# и сортировкий слиянием. Сделал его в пользу сортировки слиянием за счёт её стабильной скорости на любом массиве и
# отсутствием ограничений по памяти по условиям задачи.
# P.s алгоритм можно записать компактнее, но отдал предпочтение читабельности за счёт краткости.

# функция слияния левой и правой частей
def merger(l_list, r_list):
    sort_list = [0] * (len(l_list) + len(r_list))
    l_ind = r_ind = s_ind = 0

    while l_ind < len(l_list) and r_ind < len(r_list):
        if l_list[l_ind] <= r_list[r_ind]:
            sort_list[s_ind] = l_list[l_ind]
            s_ind += 1
            l_ind += 1
        else:
            sort_list[s_ind] = r_list[r_ind]
            s_ind += 1
            r_ind += 1
    while l_ind < len(l_list):
        sort_list[s_ind] = l_list[l_ind]
        s_ind += 1
        l_ind += 1
    while r_ind < len(r_list):
        sort_list[s_ind] = r_list[r_ind]
        s_ind += 1
        r_ind += 1
    return sort_list

# рекурсивная функция разбиения массива на 2 части
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle = len(lst) // 2
        l_list = lst[:middle]
        r_list = lst[middle:len(lst)]
        l_list = merge_sort(l_list)
        r_list = merge_sort(r_list)
        sort_list = merger(l_list, r_list)
        return sort_list

# пример тестовых данных
A = [47, 35, 117, 23, 10]
print(merge_sort(A))