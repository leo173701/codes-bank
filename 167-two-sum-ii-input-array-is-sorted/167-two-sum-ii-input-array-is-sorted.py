class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            sumvalue = numbers[left] + numbers[right]
            if sumvalue==target:
                return [left+1, right+1]
            elif sumvalue<target:
                left+=1
            else:
                right-=1