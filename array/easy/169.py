# -*- coding:utf-8 -*-
# @Time    : 2018/11/27 9:18
# @Author  : Hodge
# @Desc: 众数

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_count = {}
        result = 0
        max = 0
        for item in nums:
            if item not in dict_count:
                dict_count[item] = 1
            else:
                dict_count[item] += 1
        for item in dict_count:
            if dict_count[item] > max:
                max = dict_count[item]
                result = item
        return result

list_test = [2, 2, 1, 1, 1, 2, 2]
sl = Solution()
print(sl.majorityElement(list_test))
