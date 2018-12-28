# -*- coding:utf-8 -*-
# @Time    : 2018/12/20 16:54
# @Author  : Hodge
# @Desc:
def reverse(nums, i, j):
    while i <= j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)

        return nums


A = [1, 2, 3, 4, 5, 6, 7]
sl = Solution()
print(sl.rotate(A, 3))
