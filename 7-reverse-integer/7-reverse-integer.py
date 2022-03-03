class Solution:
    def reverse(self, x: int) -> int:
        if x>2147483647 or x<-2147483648:
            return 0
        if x<0:
            temp = -1
            x = -x
        else:
            temp = 1
        a = int(str(x)[::-1])
        if a>2147483647 or a<-2147483648:
            return 0
        return temp*a