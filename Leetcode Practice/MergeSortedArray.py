class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:])

        return nums1[:]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

x = Solution().merge(nums1, m, nums2, n)

print(nums1)