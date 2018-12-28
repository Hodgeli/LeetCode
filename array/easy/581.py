# -*- coding:utf-8 -*-
# @Time    : 2018/12/27 12:11
# @Author  : Hodge
# @Desc:

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_old = nums[:]
        nums.sort()
        # print(nums)
        # print(nums_old)
        i = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != nums_old[i]:
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != nums_old[j]:
                break
        if i <= j:
            return j - i + 1
        else:
            return 0


A = [2]
sl = Solution()
print(sl.findUnsortedSubarray(A))
