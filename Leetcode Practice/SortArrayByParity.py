class Solution:
    def sortArrayByParity(self, A):
        return sorted(A, key = lambda x: x % 2)


A = [1,2,3,4,5,8,6,5]
print(Solution().sortArrayByParity(A))