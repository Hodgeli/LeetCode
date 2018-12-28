# -*- coding:utf-8 -*-
# @Time    : 2018/12/17 10:28
# @Author  : Hodge
# @Desc:

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums) - 1
        res1 = nums[n] * nums[n - 1] * nums[n - 2]
        # res2 = nums[n] * nums[n - 1] * nums[0]
        res3 = nums[n] * nums[1] * nums[0]
        # res4 = nums[2] * nums[1] * nums[0]

        return max(res1, res3)


A = [1, 2, 3, 4]
sl = Solution()
print(sl.maximumProduct(A))
