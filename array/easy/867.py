# -*- coding:utf-8 -*-
# @Time    : 2018/11/26 16:04
# @Author  : Hodge
# @Desc:
# 给定一个矩阵 A， 返回 A 的转置矩阵。
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
import random


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        list_result = []
        col = len(A[0])
        row = len(A)
        for j in range(col):
            list_result_row = []
            for i in range(row):
                list_result_row.append(A[i][j])
            list_result.append(list_result_row)
        return list_result

A = []
seed = [0, 1, 2, 3, 4, 5]
for ii in range(2):
    list_row = []
    for i in range(3):
        list_row.append(random.choice(seed))
    A.append(list_row)
print(A)

sl = Solution()
print(sl.transpose(A))

