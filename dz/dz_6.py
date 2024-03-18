"""BINARY SEARCH"""
def binary_search(element, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            print(f'Элемент {element} найден в позиции {mid}.')
            return
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    print(f'Элемент {element} не найден в списке.')

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
element_to_find = 12
binary_search(element_to_find, arr)

"""BYBBLE SORT"""

def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr

unsorted_list = [67, 24, 9, 18, 3]
sorted_list = bubble_sort(unsorted_list)
print('Отсортированный список:', sorted_list)

#git remote add origin git@github.com:ваш_логин/название_репозитория.git
