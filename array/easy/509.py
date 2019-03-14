# -*- coding:utf-8 -*-
# @Time    : 2019/3/14 15:16
# @Author  : Hodge
# @Desc:

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = [0, 1]
        if N < 2:
            return result[N]
        else:
            for i in range(N - 1):
                result.append(result[-1] + result[-2])
        return result[N]


tester = Solution()
print(tester.fib(7))
