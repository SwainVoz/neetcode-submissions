class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_i = 1
        count_d = 1
        m_count = 1
        for c in range(1,len(nums)):
            if nums[c] > nums[c-1]:
                count_i += 1
                count_d = 1
            elif nums[c] < nums[c-1]:
                count_d += 1
                count_i = 1
            else:
                count_i = 1
                count_d = 1
            m_count = max(m_count,count_d,count_i)
        return m_count

                


        
        