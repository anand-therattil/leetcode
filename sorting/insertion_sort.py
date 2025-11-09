# Insertion Sort
# Time Complexity = O(n^2)
# Space complexity = O(1)

from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)-1):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        
    return arr

if __name__=="__main__":
    import random 
    array=[random.randint(0,100) for i in range(10)]
    print(array)
    print(insertion_sort(array))

