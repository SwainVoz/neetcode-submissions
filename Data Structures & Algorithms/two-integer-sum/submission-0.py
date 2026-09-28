class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , n in enumerate(nums):
            deff = target - n
            if deff in  hashmap:
                return[hashmap[deff],i]
            hashmap[n] = i
        return i
        
            
        

        