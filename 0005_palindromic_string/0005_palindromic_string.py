class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        input_len = cur_len = len(s)

        while cur_len > 0:
            for i in range(input_len - cur_len + 1):
                cur_value = s[i:cur_len+i]
                if cur_value == cur_value[::-1]:
                    return cur_value
            cur_len -= 1
        return None

                

print(Solution().longestPalindrome("abcbde"))