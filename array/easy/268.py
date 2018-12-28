# -*- coding:utf-8 -*-
# @Time    : 2018/11/28 15:38
# @Author  : Hodge
# @Desc:

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = len(nums)*(len(nums)+1)/2
        for item in nums:
            sum_nums -= item
        return sum_nums

list_test = [2,0,1]
sl = Solution()
print(sl.missingNumber(list_test))