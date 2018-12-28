# -*- coding:utf-8 -*-
# @Time    : 2018/12/27 15:51
# @Author  : Hodge
# @Desc:

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        nums.sort()
        n = len(nums)
        if k < 0 or n <= 1:
            return 0
        left = 0
        right = 1
        while right < n:
            num_1 = nums[left]
            num_2 = nums[right]
            temp = num_2 - num_1
            if temp < k:
                right += 1
            elif temp > k:
                left += 1
            else:
                result += 1
                while left < n and nums[left] == num_1:
                    left += 1
                while right < n and nums[right] == num_2:
                    right += 1
            if left == right:
                right += 1
        return result


list_test = [3, 1, 4, 1, 5]
sl = Solution()
print(sl.findPairs(list_test, 2))
