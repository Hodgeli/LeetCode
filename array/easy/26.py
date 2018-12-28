# -*- coding:utf-8 -*-
# @Time    : 2018/12/14 15:28
# @Author  : Hodge
# @Desc:

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        end = len(nums) - 1
        while (i < end):
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
                end -= 1
            else:
                i += 1
        return nums


A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4]
sl = Solution()
print(sl.removeDuplicates(A))
