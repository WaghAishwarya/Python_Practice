nums = [3,6,1,0]

class Solution:
    def dominantIndex(self, nums):
        x = max(nums)

        for i in nums:
            if i * 2 > x and i != x:
                return -1

        return nums.index(x)


print(Solution().dominantIndex(nums))