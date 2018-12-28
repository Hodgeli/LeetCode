# -*- coding:utf-8 -*-
# @Time    : 2018/12/18 9:27
# @Author  : Hodge
# @Desc:

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ou = 0
        ji = 1
        i = len(A) - 1
        while i >= ou and i >= ji:
            if A[i] % 2 == 0:
                temp = A[ou]
                A[ou] = A[i]
                A[i] = temp
                ou += 2
            else:
                temp = A[ji]
                A[ji] = A[i]
                A[i] = temp
                ji += 2
        return A

A = [1, 2, 3, 4]
sl = Solution()
print(sl.sortArrayByParityII(A))
