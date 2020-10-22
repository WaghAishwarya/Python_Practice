class Solution(object):
    def threesum(self, nums):
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = length-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if not total:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l + 1]:
                        l += 1
                    while nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif total < 0:
                    l = l + 1
                else:
                    r = r - 1
        return res

nums = [-25,-10,-7,-3,2,4,8,10]
s = Solution().threesum(nums)
print(s)