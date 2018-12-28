# -*- coding:utf-8 -*-
# @Time    : 2018/11/28 16:55
# @Author  : Hodge
# @Desc:

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


list_test = [7, 5, 3, 6, 4,1]
sl = Solution()
print(sl.maxProfit(list_test))
