class Solution:
    def pivotInteger(self, n: int) -> int:
        i = 1
        j = n
        ival = 1 
        jval = n
        while i <= j :
            if i == j and ival == jval :
                return i 
            i += 1
            ival += i
            if ival > jval:
                j -= 1
                jval += j

        return -1
        
