# -*- coding:utf-8 -*-
# @Time    : 2018/11/27 9:06
# @Author  : Hodge
# @Desc: 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True



matrix = [
    [1, 2, 3, 4],
    [5, 2, 2, 3],
    [9, 5, 1, 2]
]
sl = Solution()
print(sl.isToeplitzMatrix(matrix))
