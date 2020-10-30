class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0

        while i < len(arr)-1:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 2
            else:
                i += 1


arr = [1,0,2,3,0,4,5,0]
x = Solution().duplicateZeros(arr)
print(arr)