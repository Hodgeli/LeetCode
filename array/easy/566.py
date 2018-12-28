# -*- coding:utf-8 -*-
# @Time    : 2018/11/26 17:56
# @Author  : Hodge
# @Desc:
import random


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        n = row * col

        if r * c != n:
            return nums
        else:
            list_result = [[0]*c for i in range(r)]
            for i in range(row):
                for j in range(col):
                    list_result[(i * col + j) / c][(i * col + j) % c] = nums[i][j]
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
print(sl.matrixReshape(A, 3, 2))
