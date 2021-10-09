class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2**31 or x > 2**31 -1:
            return 0
        
        ## boundary value 0 must be included else will cause error to convert None to int
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            print(x)
            ans = int(str(x)[:0:-1])*-1

        if ans < -2**31 or ans > 2**31 -1:
            return 0
        
        return ans


print(Solution().reverse(0))