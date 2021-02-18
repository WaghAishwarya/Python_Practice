class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()

        if len(x) != 0:
            return len(x[-1])
        else:
            return 0

print(Solution().lengthOfLastWord("abcd abcdf efbg"))
print(Solution().lengthOfLastWord("abcd abcdf efbg kbs"))
print(Solution().lengthOfLastWord("abcd abcdf efbgih gh"))