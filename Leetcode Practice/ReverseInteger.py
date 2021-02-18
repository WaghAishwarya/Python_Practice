class Solution:
    def reverse(self, x: int) -> int:

        y = str(x)
        if x >= 2147483648 or x <= -2147483647:
            return 0
        else:
            if x >= 0:
                rev = int(y[::-1])

            else:
                t1 = y[1:]
                t2 = t1[::-1]
                rev = int('-' + t2)

            if rev >= 2147483648 or rev <= -2147483647:
                return 0
            else:
                return rev

print(Solution().reverse(27))
print(Solution().reverse(-1013))
print(Solution().reverse(-10145))
print(Solution().reverse(1103456671))