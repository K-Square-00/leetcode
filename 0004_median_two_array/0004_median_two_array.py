class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1 + nums2)
        max_value = max(nums1+nums2) + 1
        ans = []
        upper_index, lower_index, cur_index = 0, 0, 0

        if total_len % 2 == 0:
            upper_index, lower_index =  int(total_len/2) , int(total_len/2 -1)
        else:
            upper_index = lower_index  = int(total_len/2)
        
        nums1.append(max_value)
        nums2.append(max_value)

        while cur_index <= upper_index:
            
            if nums1[0] < nums2[0]:
                value = nums1[0]
                nums1.pop(0)
            else:
                value = nums2[0]
                nums2.pop(0)               
            
            if cur_index == lower_index or cur_index == upper_index:
                ans.append(float(value))
            
            cur_index += 1
        
        return sum(ans)/len(ans)


#print(Solution().findMedianSortedArrays([1,2],[3,4]))