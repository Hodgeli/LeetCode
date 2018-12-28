# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 16:16
# @Author  : Hodge
# @Desc:

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = temp_k = sum(nums[:k])
        for i in range(k, len(nums)):
            temp_k = temp_k - nums[i - k] + nums[i]
            result = max(result, temp_k)
        return float(result) / k


A = [1,12,-5,-6,50,3]
sl = Solution()
print(sl.findMaxAverage(A, 4))
