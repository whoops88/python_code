"""
input:
3 8
2 8 8
3, 4, 5, 5, 10, 11, 12,12

output:
2, 3, 4, 5, 5, 8, 8, 10, 11, 12, 12
"""

m, n = map(int, input().split())
list_m = list(map(int, input().split()))
list_n = list(map(int, input().split()))
list_output = []
m_index = 0
n_index = 0

while m_index < m and n_index < n:
    if list_m[m_index] < list_n[n_index]:
        list_output.append(list_m[m_index])
        m_index +=1
    else:
        list_output.append(list_n[n_index])
        n_index+=1
while m_index < m:
    list_output.append(list_m[m_index])
    m_index +=1

while n_index < n:
    list_output.append(list_n[n_index])
    n_index+=1

print(*list_output)