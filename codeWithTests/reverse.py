class Solution:
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not isinstance(x,int):
            raise TypeError('x must be of type int.')

        sign = 1
        if x<0:
            sign = -1
          
        s = str(abs(x)) 
        i = len(s)-1
        rs = ''
        
        while (i>=0):
            rs += s[i]
            i-=1;
            
        rx = int(rs)

        if (rx>2147483648):
            return 0
        
        return rx*sign 



            