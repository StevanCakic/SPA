def short_string(input_string, limit):
    if len(input_string) > limit:
        return input_string[:limit + 1] + "..."

def sum_of_odd_squared(start_segment, end_segment):
    suma = 0
    for i in range(start_segment, end_segment + 1):
        if i % 2 != 0:
            suma= suma + (i * i)
    return suma

def longest_increasing(input_list):
    duz_max = 0
    konacna = []
    for i in range(0, len(input_list)):
        d = 0
        lista = []
        for j in range(i, len(input_list)):
            current_element = input_list[j]
            if current_element < input_list[j-1] and j != i:
                break
            if current_element > 0:
                lista.append(current_element)
                d = d + 1
        if d > duz_max:
            duz_max = d
            konacna = lista.copy()
    return konacna

print(short_string("Radim kolokvijum iz programiranja", 15))
print(short_string("Danas idem na laboratoriske vjezbe", 10))

print(sum_of_odd_squared(2, 9))
print(sum_of_odd_squared(1, 5))

print(longest_increasing([1, 2, 3, -1, 0, 5, 6, 7, 10, 10, 1]))
print(longest_increasing([0, 1, 1, 0, 5, 6, 7, 8]))