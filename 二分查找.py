def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if item == guess:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
my_item = 3
print(binary_search(my_list, my_item))