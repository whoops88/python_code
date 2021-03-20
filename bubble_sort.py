from random import randint

n = 10
a = [randint(1, 99) for i in range(n)]
print(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

m = 11
b = [randint(1, 99) for i in range(m)]
print(b)
i = 0
while i < m - 1:
    j = 0
    while j < m - i - 1:
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
        j += 1
    i += 1
print(b)

c = [randint(1, 99) for i in range(m)]
print(c)


def bubble_sort(array):
    n = len(array)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return print(array)


bubble_sort(c)