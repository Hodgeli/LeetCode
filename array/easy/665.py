# -*- coding:utf-8 -*-
# @Time    : 2018/12/28 9:36
# @Author  : Hodge
# @Desc:

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if count > 1:
                return False
            if nums[i] < nums[i - 1]:
                count += 1
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True


list_test = [4, 2, 1]
sl = Solution()
print(sl.checkPossibility(list_test))
