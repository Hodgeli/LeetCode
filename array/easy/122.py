# -*- coding:utf-8 -*-
# @Time    : 2018/11/28 15:25
# @Author  : Hodge
# @Desc:

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result

list_test = [1, 7, 2, 3, 6, 7, 6, 7]
sl = Solution()
print(sl.maxProfit(list_test))
