# -*- coding:utf-8 -*-
# @Time    : 2018/12/14 16:20
# @Author  : Hodge
# @Desc:

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in xrange(len(nums)):
            if nums[i] >= target:
                return i


A =  [1,3,5,6]
sl = Solution()
print(sl.searchInsert(A,7))
