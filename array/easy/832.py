# -*- coding:utf-8 -*-
# @Time    : 2018/11/26 15:00
# @Author  : Hodge
# @Desc:
#   给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#   水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#   反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
import random


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, row in enumerate(A):
            row.reverse()
            for j, item in enumerate(row):
                A[i][j] = (item + 1) % 2
        return A


A = []
seed = [0, 1]
for ii in range(3):
    list_row = []
    for i in range(3):
        list_row.append(random.choice(seed))
    A.append(list_row)
print(A)

sl = Solution()
sl.flipAndInvertImage(A)
