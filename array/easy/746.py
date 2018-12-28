# -*- coding:utf-8 -*-
# @Time    : 2018/12/18 18:19
# @Author  : Hodge
# @Desc:

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        totol = []
        totol.append(cost[0])
        totol.append(cost[1])
        for i in range(2, len(cost)):
            totol.append(min((totol[i - 2] + cost[i]), (totol[i - 1] + cost[i])))
        return min(totol[len(cost) - 1], totol[len(cost) - 2])


A = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sl = Solution()
print(sl.minCostClimbingStairs(A))
