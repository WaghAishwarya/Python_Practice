class Solution():
    def replaceElements(self, x):
        y = [0] * len(x)
        y[-1] = -1

        for i in range(len(x)-2, -1, -1):
            y[i] = max(y[i+1], x[i+1])
        return y


x = [15,16,1,2,5,3,4]


print(Solution().replaceElements(x))
