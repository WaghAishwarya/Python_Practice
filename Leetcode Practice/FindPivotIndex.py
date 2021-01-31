class Solution():
    def pivotIndex(self, nums):

        x = sum(nums)
        print(x)
        l_sum = 0
        for i, num in enumerate(nums):
            if l_sum == (x-l_sum-num):
                return i
            l_sum += num
        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))