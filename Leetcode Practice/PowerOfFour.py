import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return (math.log10(n) / math.log10(4)) % 1 == 0
        # while n != 1:
        #     if n % 4 != 0:
        #         return False
        #     n = n//4
        # return True

print(Solution().isPowerOfFour(16))
print(Solution().isPowerOfFour(64))
print(Solution().isPowerOfFour(160))