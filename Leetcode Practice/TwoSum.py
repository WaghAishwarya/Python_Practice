class Solution:
    def twoSum(self, nums: [int] , target: int):
        a = {}
        result = []
        for i, num in enumerate(nums):
            if a.get(num) is None:
                a[target-num] = i
            else:
                result = [a[num], i]
        return result

l = Solution()
print(l.twoSum([2, 5, 7, 11, 20], 27))
print(l.twoSum([5, 6], 11))
print(l.twoSum([2, 7 ,11, 15], 26))
print(l.twoSum([2, 7 ,11, 15], 27))