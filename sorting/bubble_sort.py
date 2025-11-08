# Bubble Sort
# Time Complexity = O(n^2)
# Space complexity = O(1)
# The Swap section is present for the optimization, but it is not required 

from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i -1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr

if __name__=="__main__":
    import random 
    array=[random.randint(0,100) for i in range(10)]
    print(array)
    print(bubble_sort(array))

