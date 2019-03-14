# -*- coding:utf-8 -*-
# @Time    : 2019/1/7 17:17
# @Author  : Hodge
# @Desc:

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        temp = [[]]
        result = []
        for i in range(1, 10):
            for item in temp[:]:
                temp.append(item+[i])
        for item in temp:
            if len(item) == k and sum(item) == n:
                result.append(item)
        return result


tester = Solution()
print(tester.combinationSum3(3, 9))
