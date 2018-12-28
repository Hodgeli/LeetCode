# -*- coding:utf-8 -*-
# @Time    : 2018/12/16 18:24
# @Author  : Hodge
# @Desc:

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分治法
        # n = len(nums)
        # mid = n // 2
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(max(nums), nums[0]+nums[1])
        # else:
        #     nums_left, nums_right = nums[:mid], nums[mid + 1:]
        #     max_left, max_right = self.maxSubArray(nums_left), self.maxSubArray(nums_right)
        #     sum = 0
        #     max_sum_left = float('-inf')
        #     max_sum_right = float('-inf')
        #     for i in range(mid, -1, -1):
        #         sum += nums[i]
        #         max_sum_left = max(max_sum_left, sum)
        #     sum = 0
        #     for i in range(mid, n):
        #         sum += nums[i]
        #         max_sum_right = max(max_sum_right, sum)
        #     return max(max_left, max_right, max_sum_left + max_sum_right - nums[mid])

        sum = 0
        result = nums[0]
        for num in nums:
            sum += num
            result = max(sum,result)
            if sum <= 0:
                sum = 0
        return result

A = [1]
sl = Solution()
print(sl.maxSubArray(A))
