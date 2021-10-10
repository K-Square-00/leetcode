class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        input_str = s.lstrip()

        sign = '+'
        
        if len(input_str) > 0 and input_str[0] in ('+','-'):
            sign = input_str[0]
            input_str = input_str[1:]

        i = 1
        input_num = 0
        while i < len(input_str)+1:
            if input_str[:i].isdigit():
                input_num = input_str[:i]
                i+=1
            else:
                break
        
        if sign == '-':
            ans =  int(input_num)*-1
        else:
            ans = int(input_num)

        if ans < -2**31:
            ans = -2**31

        if ans > 2**31-1:
            ans = 2**31 -1

        return ans
        

print(Solution().myAtoi("words and 987"))