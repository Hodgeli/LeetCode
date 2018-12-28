# -*- coding:utf-8 -*-
# @Time    : 2018/11/26 16:35
# @Author  : Hodge
# @Desc:
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result


arr = raw_input()
num = [int(n) for n in arr.split()]
print(num)
sl = Solution()
print(sl.arrayPairSum(num))
