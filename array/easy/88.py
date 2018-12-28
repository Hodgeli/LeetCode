# -*- coding:utf-8 -*-
# @Time    : 2018/12/14 16:40
# @Author  : Hodge
# @Desc:

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()
        return nums1


A = [1, 2, 3, 0, 0, 0]
B = [2, 5, 6]
sl = Solution()
print(sl.merge(A, 3, B, 3))
