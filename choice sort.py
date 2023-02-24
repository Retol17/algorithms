# сортировка выбором
a = [3,51,1,35,2678,34,612,134,2]
for i in range(0,len(a)-1):
    min_index = i
    for j in range(i+1,len(a)):
        if a[min_index] > a[j]:
            min_index = j
    if min_index != i:
        temp = a[min_index]
        a[min_index] = a[i]
        a[i]  = temp
print(a)