## Brute Force Sort or Selective Sort
# Time Complexity = O(n^2) as we are going through the array twice
# Space complexity = O(1) only a temporary variable is used for swapping

from typing import List
def brute_force(array:List=None):
    if array is None:
        return None
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    return array

# if __name__=="__main__":
#     import random 
#     array=[random.randint(0,100) for i in range(10)]
#     print(array)
#     print(brute_force(array))


