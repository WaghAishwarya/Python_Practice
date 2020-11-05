class Solution:
    def checkIfExist(self, arr) -> bool:
        if 0 in arr and arr.count(0) > 1:
            return True
        for i in arr:
            if i and i*2 in arr:
                return True
        return False


arr1 = [7,1,14,11]
x = Solution().checkIfExist(arr1)
print(x)
arr2 = [10,2,5,3]
y = Solution().checkIfExist(arr2)
print(y)
arr3 = [3,1,7,11]
z = Solution().checkIfExist(arr3)
print(z)