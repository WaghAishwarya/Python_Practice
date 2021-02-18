import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return (math.log10(n) / math.log10(2)) % 1 == 0
        # while n != 1:
        #     if n % 2 != 0:
        #         return False
        #     n = n//2
        # return True


print(Solution().isPowerOfTwo(27))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(5))
print(Solution().isPowerOfTwo(8))