class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i, j, ans, cur_len = 0, 0, 0, 0
        dict_repeat = {}

        for index, value in enumerate(s):

            if value not in dict_repeat or dict_repeat[value] < i:
                cur_len += 1
                ans = max(ans, cur_len)
                
            else:   
                i = dict_repeat[value] + 1
                cur_len = j - i + 1
            
            j += 1
            dict_repeat[value] = index
            
        return ans

#print(Solution().lengthOfLongestSubstring("tmmzuxt"))