# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 15:52
# @Author  : Hodge
# @Desc:

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超时
        # for i in range(len(nums)):
        #     count_left = sum(nums[:i])
        #     count_right = sum(nums[i+1:])
        #     if count_left == count_right:
        #         return i
        # return -1

        sum_all = sum(nums)
        count = 0
        for i in range(len(nums)):
            if 2*count+nums[i] == sum_all:
                return i
            else:
                count += nums[i]
        return -1


A = [1,7,3,6,5,6]
sl = Solution()
print(sl.pivotIndex(A))
