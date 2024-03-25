"""BINARY SEARCH"""
import random 

def binary_search(val):
    n = 5000 
    resultOk = False 
    first = 0
    last = n - 1 
    while first < last:
        middle = (first+last)//2
        if val == middle:
            first = middle
            last=first
            resultOk = True
            pos = middle
        else:
            if val>middle:
                first=middle+1
            else:
                last=middle-1
                
    if resultOk:
        print('Элемент найден')
        print(pos)
    else:
        print('Элемент не найден')
        
    
val = random.randint(0, 5000)
print(val)
binary_search(val)




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