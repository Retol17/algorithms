import time
# сортировка пузырьком
t0 = time.clock()
a = [3,51,1,35,2678,34,612,134,2]
lenght = len(a)
while lenght != 0:
    max_index = 0
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            s = a[i-1]
            a[i-1] = a[i]
            a[i] = s
            max_index = i
    lenght = max_index
t1 = time.clock()- t0
print(t1)
