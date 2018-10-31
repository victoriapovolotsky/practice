class MyAtoi:

    def my_atoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        s = str.strip(' ')
        l = len(s)
        sign = 1
        i = 0

        if l == 0:
            return 0
        elif s[0] == '+':
            sign = 1
            i = 1
        elif s[0] == '-':
            sign = -1
            i = 1
        
        myatoi = ''

        for j in range (i,l):
            try:
                int(s[j])
                myatoi += s[j]

            except:
                break;

        if len(myatoi)>0:
            return MyAtoi.check_out_of_bounds(myatoi, sign)
        else:
            return 0;


    def check_out_of_bounds(myatoi, sign):
        myatoi_int = sign*int(myatoi)
        if myatoi_int >= 2147483647:
            return 2147483647
        if myatoi_int <= -2147483648:
            return -2147483648
        else:
            return myatoi_int


