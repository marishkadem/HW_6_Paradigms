
"""
Бинарный поиск в структурной и процедурной парадигмах. Создание списка случайных значений и его сортировка - декларативный стиль.
"""
def binary_search(list: list[int], num: int) -> int:
    begin = 0
    end = len(list) - 1
    while begin <= end:
        middle = begin + (end - begin) // 2
        if num == list[middle]:
            return middle
        if num < list[middle]:
            end = middle - 1
        if num > list[middle]:
            begin = middle + 1
    return -1


if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(50)]
    lst.sort()
    print(lst)
    print(binary_search(lst, 13))