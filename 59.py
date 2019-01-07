# -*- coding:utf-8 -*-
# @Time    : 2019/1/7 16:02
# @Author  : Hodge
# @Desc:直接转圈圈填充

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for col in range(n)] for row in range(n)]
        num = 1
        times = 0
        while (num <= n * n):
            for i in range(times, n - times):
                result[times][i] = num
                num += 1
            if num > n*n:
                break
            for i in range(times+1,n-times-1):
                result[i][n-times-1] = num
                num += 1
            for i in range(n - times-1,times-1,-1):
                result[n-times-1][i] = num
                num += 1
            for i in range(n-times-2,times,-1):
                result[i][times] = num
                num += 1
            times += 1
        return result


test = 4
tester = Solution()
print(tester.generateMatrix(test))
