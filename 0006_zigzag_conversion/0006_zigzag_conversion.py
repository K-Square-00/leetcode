class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        len_s = len(s)
        end = " "
        x,y = 0,0
        
        makeTurn = False
        max_step = numRows -1
        cur_step = 0
        dict = {}
        ans = []


        
        for i,c in enumerate(s):
    
            dict[str(y)+"-"+str(x)] = c
            print(x,y)
            if cur_step == max_step:
                makeTurn = not makeTurn
                cur_step = 1
            else:
                cur_step += 1
            
            if makeTurn:
                x,y = x+1, y-1
            else:
                x,y = x, y+1

        for i in range(numRows):
            for j in range(x+1):
                dict_key = str(i) + "-" + str(j)
                if dict_key in dict:
                    ans.append(dict[dict_key])
            

        return "".join(ans)



print(Solution().convert("AB",1))