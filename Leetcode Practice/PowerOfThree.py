import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        return (math.log10(n) / math.log10(3)) % 1 == 0
        # if n <= 0:
        #     return False
        # elif n % 2 == 0:
        #     return False
        #
        # while n % 3 == 0:
        #     n /= 3
        #
        # if n == 1:
        #     return True
        # else:
        #     return False

print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(16))
print(Solution().isPowerOfThree(5))
print(Solution().isPowerOfThree(243))