class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums

x = [1,5,0,6,0,3,8,0]
y = [0,0,1]  #To handle this Testcase we use [::-1] to iterate the list from the back to front. Iterating list inversely to avoid skipping lists elements.
print(Solution().moveZeroes(x))
print(Solution().moveZeroes(y))