y = [67, 8, 9, 0, 10, 145, 773, 234, 654, 43, 3, 4]
y = sorted(y)


def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        center = (lower_bound + upper_bound) // 2
        if array[center] == value:
            return f"{center}-th element "
        elif array[center] > value:
            upper_bound = center - 1
        elif array[center] < value:
            lower_bound = center + 1
    return "There is no such element"


print(binary_search(y, 43))