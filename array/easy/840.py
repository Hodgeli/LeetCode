# -*- coding:utf-8 -*-
# @Time    : 2018/12/27 9:43
# @Author  : Hodge
# @Desc:

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row - 2):
            for j in range(col - 2):
                set_9 = set([])
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        if grid[ii][jj] in [x for x in range(1,10)]:
                            set_9.add(grid[ii][jj])
                if len(set_9) != 9:
                    continue
                row_1 = sum(grid[i][j:j + 3])
                row_2 = sum(grid[i + 1][j:j + 3])
                row_3 = sum(grid[i + 2][j:j + 3])
                col_1 = sum([x[j] for x in grid[i:i + 3]])
                col_2 = sum([x[j + 1] for x in grid[i:i + 3]])
                col_3 = sum([x[j + 2] for x in grid[i:i + 3]])
                xie_1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                xie_2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
                if row_1 == row_2 and row_2 == row_3 and row_3 == col_1 and col_1 == col_2 and col_2 == col_3 and col_3 == xie_1 and xie_1 == xie_2:
                    result += 1
        return result


A = [[5,5,5],[5,5,5],[5,5,5]]
sl = Solution()
print(sl.numMagicSquaresInside(A))
