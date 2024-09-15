arrays = [1, 2, 3, 4, 78, 8, 4]
def bubble_sort(ls):
        for i in range(len(ls) - 1, 0, -1):
            for j in range(i):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]

        return ls


def selection_sort(ls):
    for i in range(len(ls) - 1):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
                ls[j], ls[lowest] = ls[lowest], ls[j]
    return ls

def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >=  0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls

