class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        while n%5==0:
            n = n//5
            # print("n =n//5 = ",n)
        while n%3==0:
            n=n//3
            # print("n =n//3 = ",n)
        while n%2==0:
            n=n//2
        if n in {1,2,4,5,6,8,9,10,12,15,16,18,20}:
            return True
        return False