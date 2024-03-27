class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        comp = {1, 2, 3,5}
        d = 2
        while n > 1:
            if n %d == 0:
                n //=  d
                
            elif d == 2:
                d = 3 
            elif d == 3:
                d = 5
            else:
                return False

        return True
        