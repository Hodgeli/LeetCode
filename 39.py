# -*- coding:utf-8 -*-
# @Time    : 2019/1/7 17:55
# @Author  : Hodge
# @Desc:

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, [])
        return res

    def dfs(self, candidate, target, res, temp):
        if target < 0:
            return
        elif target == 0:
            res.append(temp)
            return
        else:
            for cand in candidate:
                if cand > target:
                    return
                if not temp or cand >= temp[-1]:
                    self.dfs(candidate, target - cand, res, temp + [cand])
        return


candidates = [2, 3, 6, 7]
target = 7
tester = Solution()
print(tester.combinationSum(candidates, target))
