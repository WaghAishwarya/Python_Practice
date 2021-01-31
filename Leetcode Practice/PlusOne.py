class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i]+=1
            if digits[i] < 10:

                return digits
            else:
                digits[i] = 0


        digits.insert(0,1)
        return digits


nums = [1,2,4,4]
y = [0,0]
x = [9]
print(Solution().plusOne(nums))
print(Solution().plusOne(y))
print(Solution().plusOne(x))