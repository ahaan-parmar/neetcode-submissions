class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexmap = {} #we map it as val->indeex

        for i,n in enumerate(nums):
            indexmap[n] = i
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in indexmap and indexmap[dif] != i:
                return [i, indexmap[dif]]
        return []