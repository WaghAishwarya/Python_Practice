class Solution:
    def findNumbers(self, nums) -> int:
        count = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count


nums = [12,6,8,200.22,1964]
x = Solution().findNumbers(nums)
print(x)