# -*- coding:utf-8 -*-
# @Time    : 2018/12/28 10:15
# @Author  : Hodge
# @Desc:DFS算法，构建二叉树遍历到叶子节点

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        n = len(nums)
        for i in range(n):
            temp = result[:]
            for item in temp:
                result.append(item + [nums[i]])

        return result


test = []
tester = Solution()
print(tester.subsets(test))
