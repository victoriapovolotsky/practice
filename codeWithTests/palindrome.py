class Palindrome:
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if not isinstance(x,int):
            raise TypeError('x must be of type int.')

        s = str(x)
        l = len(s)
        if l == 1:
            return True
        
        for i in range(l):
            j = l-i-1;
            if i>j:
                return True
            if s[i]!=s[j]:
                return False