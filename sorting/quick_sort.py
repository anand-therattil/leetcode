# Insertion Sort
# Time Complexity = O(nlog(n)) worst case O(N^2)
# Space complexity = O(n) worst case avg case O(log(n))

from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr)<=1: 
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
        
if __name__=="__main__":
    import random 
    array=[random.randint(0,100) for i in range(10)]
    print(array)
    print(quick_sort(array))

