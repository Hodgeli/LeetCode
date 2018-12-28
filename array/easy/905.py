# -*- coding:utf-8 -*-
# @Time    : 2018/11/18 18:21
# @Author  : Hodge
# @Desc: 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。你可以返回满足此条件的任何数组作为答案。

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flag = 0;
        for i, item in enumerate(A):
            if item % 2 == 0:
                temp = A[flag]
                A[flag] = A[i]
                A[i] = temp
                flag += 1
        return A


arr = raw_input()
num = [int(n) for n in arr.split()]
print(num)
sl = Solution()
print(sl.sortArrayByParity(num))
