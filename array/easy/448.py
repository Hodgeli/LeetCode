# -*- coding:utf-8 -*-
# @Time    : 2018/12/11 16:09
# @Author  : Hodge
# @Desc:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_result = [i + 1 for i in range(len(nums))]
        return list(set(list_result) ^ set(nums))


list_test = [4, 3, 2, 7, 8, 2, 3, 1]
sl = Solution()
print(sl.findDisappearedNumbers(list_test))
