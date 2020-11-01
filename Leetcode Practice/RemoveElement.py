class Solution:
    def removeElement(self, nums, val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)

nums = [3,2,2,3]
val = 3
x = Solution().removeElement(nums, val)
print(x)
print(nums)