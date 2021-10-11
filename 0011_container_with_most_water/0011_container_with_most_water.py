class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area, start_index, end_index = 0, 0, len(height) - 1

        while start_index < end_index:
            cur_width = end_index - start_index
            cur_height = min(height[start_index],height[end_index])
            cur_area = cur_width * cur_height

            max_area = max(max_area, cur_area)

            if height[start_index] > height[end_index]:
                end_index -= 1
            else:
                start_index += 1
            
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))