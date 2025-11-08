# Merge Sort
# Time Complexity = O(nlog(n))
# Space complexity = O(n) 

from typing import List



def merge(arr:List,low:int,mid:int,high:int):
    left = low 
    right = mid+1
    temp = []
    while(left<=mid and right<=high):
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return arr 

def merge_sort(arr:List,low:int,high:int):
    mid = (low+high)//2
    if (low>=high):
        return arr
    else:
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
    return arr

if __name__=="__main__":
    import random 
    array=[random.randint(0,100) for i in range(10)]
    print(array)
    low = 0
    high = len(array)-1
    print(merge_sort(array,low,high))

