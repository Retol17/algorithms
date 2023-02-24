def sort(array):
    lower = []
    upper = []
    middle = []
    if len(array) > 1:
        elem = array[0]
        for i in array:
            if i < elem:
                lower.append(i)
            elif i == elem:
                middle.append(i)
            elif i > elem:
                upper.append(i)
        return sort(lower) + middle + sort(upper)
    return array
a = [7, 5, 3, 1, 4, 9, 3, 2]
print(sort(a))