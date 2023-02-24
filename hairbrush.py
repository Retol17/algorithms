def mySort(A):
    step = len(A) - 1
    while step > 0:
        for i in range(0, len(A)-step):
            if (A[i] > A[i+step]):
                A[i], A[i+step] = A[i+step], A[i]
        step = int(step//1.25)
    return A

a = [7, 5, 3, 1, 4, 9, 3, 2]
print(mySort(a))