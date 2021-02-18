class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)

        if str(x) == y[::-1]:
            return True
        return False


print(Solution().isPalindrome(27))
print(Solution().isPalindrome(101))
print(Solution().isPalindrome(-101))
print(Solution().isPalindrome(10))