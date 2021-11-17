class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:
            return "1"
        factory = []
        temp =1
        nums = []

        for i in range(1,n):
            nums.append(i)
            temp *=i
            factory.append(temp)
        nums.append(n)
        res = ""
        i=1
        while i<n:
            solution, remainder = k//factory[-i], k%factory[-i] 
            # print("solution = ",solution)
            # print("remainder = ",remainder)
            if solution!=0 :
                if remainder!=0:
                    a = nums[solution]
                    res +=str(a)
                    i +=1
                    k = remainder
                    nums.remove(a)
                    # print("nums = ",nums)
                else:
                    a = nums[solution-1]
                    res +=str(a)
                    nums.remove(a)
                    nums.sort(reverse = True)
                    for m in nums:
                        res +=str(m)
                    # print("nums = ",nums)
                    return res
            else:
                a = nums[solution]
                res +=str(a)
                i +=1
                k = remainder
                nums.remove(a)
                # print("nums = ",nums)
        return res