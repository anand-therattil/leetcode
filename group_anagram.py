from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        else:
            result = defaultdict(list)
            for i in strs:
                count = [0]*26
                for c in i: 
                    count[ord(c)-ord('a')] +=1
                key= tuple(count)
                result[key].append(i)
                print(result.values())
            return list(result.values())