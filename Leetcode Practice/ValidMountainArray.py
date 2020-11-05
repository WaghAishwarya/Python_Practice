class Solution:
    def validMountainArray(self, A) -> bool:

        if len(A) < 3:
            return False

        if A[0] > A[1]:
            return False

        index = A.index(max(A))
        if index == 0 or index == len(A) - 1:
            return False

        for i in range(0, index):
            if A[i] >= A[i + 1]:
                return False

        for i in range(index + 1, len(A)):
            if A[i] >= A[i - 1]:
                return False
        return True

A = [2,1]
x = Solution().validMountainArray(A)
print(x)
A1 = [3,5,5]
y = Solution().validMountainArray(A1)
print(y)
A2 = [0,3,2,1]
z = Solution().validMountainArray(A2)
print(z)