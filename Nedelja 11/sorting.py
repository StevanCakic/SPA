
def selection_sort(data):
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                # data[i], data[j] = data[j], data[i]
                tmp = data[j]
                data[j] = data[i]
                data[i] = tmp
    return data

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


print(selection_sort([3, 1, 7, 2]))
print(bubble_sort([3, 1, 7, 2]))


