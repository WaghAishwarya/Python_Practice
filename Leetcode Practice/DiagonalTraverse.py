class Solution:
    def findDiagonalOrder(self, matrix: list[list[int]]):

        m = len(matrix)

        n = len(matrix[0]) if m > 0 else 0

        if n == 0:
            return []

        result = [0 for i in range(m*n)]
        row = col = 0
        up = True

        for i in range(m*n):
            result[i] = matrix[row][col]

            if up:
                if col == n-1:
                    row = row+1
                    up = not up

                elif row == 0:
                    col = col+1
                    up = not up

                else:
                    row = row-1
                    col = col+1

            else:
                if row == m-1:
                    col = col+1
                    up = not up

                elif col == 0:
                    row = row+1
                    up = not up

                else:
                    row = row+1
                    col = col-1

        return result

#
# if len(matrix) == 0 or len(matrix[0]) == 0:
#     return []
# m, n = len(matrix), len(matrix[0])
# r, c = 0, 0
# res = []
# for i in range(m * n):
#     res.append(matrix[r][c])
#     if (r + c) % 2 == 0:
#         if c == n - 1:
#             r += 1
#         elif r == 0:
#             c += 1
#         else:
#             r -= 1
#             c += 1
#     else:
#         if r == m - 1:
#             c += 1
#         elif c == 0:
#             r += 1
#         else:
#             c -= 1
#             r += 1
# return res
# m, n = len(matrix), len(matrix[0])
#
# r, c = 0, 0
# res = list()
# for i in range(m * n):
#     res.append(matrix[r][c])
#     if (r + c) % 2 == 0:
#         # going up
#         if c == n - 1:
#             r += 1
#         elif r == 0:
#             c += 1
#         else:
#             r -= 1
#             c += 1
#     else:
#         # going down
#         if r == m - 1:
#             c += 1
#
#         elif c == 0:
#             r += 1
#         else:
#             r += 1
#             c -= 1
# return res

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(Solution().findDiagonalOrder(x))