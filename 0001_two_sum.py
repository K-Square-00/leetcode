class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        
        i = 0
        for n in nums:
            m = target - n
            if m in dict:
                return [dict[m],i]
            dict[n] = i
            i+=1
            
        return None

