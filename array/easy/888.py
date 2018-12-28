# -*- coding:utf-8 -*-
# @Time    : 2018/12/11 16:19
# @Author  : Hodge
# @Desc:
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        diff = (sum_A - sum_B) / 2
        set_B = set(B)
        for i in A:
            if i - diff in set_B:
                return [i, i - diff]


A = [1, 1]
B = [2, 2]
sl = Solution()
print(sl.fairCandySwap(A, B))
