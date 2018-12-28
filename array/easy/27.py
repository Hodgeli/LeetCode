# -*- coding:utf-8 -*-
# @Time    : 2018/11/27 9:51
# @Author  : Hodge
# @Desc:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        flag = 0
        for i, item in enumerate(nums):
            if item == val:
                temp = nums[flag]
                nums[flag] = item
                nums[i] = temp
                flag += 1
        nums.reverse()
        return len(nums)-flag


nums = [0, 1, 2, 2, 3, 0, 4, 2]
sl = Solution()
print(sl.removeElement(nums, 2))
