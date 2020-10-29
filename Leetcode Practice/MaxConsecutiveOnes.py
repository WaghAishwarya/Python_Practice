class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                result = max(result, count)
            else:
                count = 0
        return result

nums = [1,0,1,0,1,1,0,0,1,1,1,1]
x = Solution().findMaxConsecutiveOnes(nums)
print(x)

