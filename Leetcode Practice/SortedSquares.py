class Solution:
    def sortedSquares(self, A):
        result = sorted(i ** 2 for i in A)
        return result

A = [-1,-4,0,3,10]
x = Solution().sortedSquares(A)
print(x)