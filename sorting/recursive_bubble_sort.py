# Recursive Bubble Sort
# Time Complexity = O(n^2)
# Space complexity = O(1)
# The Swap section is present for the optimization, but it is not required 

from typing import List

def rec_bubble_sort(arr: List[int], n:int=None) -> List[int]:
    if n is None:
        n = len(arr)
    if n==1:
        return arr

    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    return rec_bubble_sort(arr,n-1)

if __name__=="__main__":
    import random 
    array=[random.randint(0,100) for i in range(10)]
    print(array)
    print(rec_bubble_sort(array))

