# Бинарный поиск
a = [1,2,3,4,5,6,6,7,8,10,14,16,21,155,170,502]
def binnaray_search(list,item):
    high = len(list) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
    return 0
print('-----',binnaray_search(a,6))




