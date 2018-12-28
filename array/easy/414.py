# -*- coding:utf-8 -*-
# @Time    : 2018/12/26 17:45
# @Author  : Hodge
# @Desc:

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        # print(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            nums = list(nums)
            nums.sort()
            # print(nums)
            return nums[-3]

A = [5,5,5,5,-2,4,-1,2,1,0]
sl = Solution()
print(sl.thirdMax(A))