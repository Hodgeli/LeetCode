# -*- coding:utf-8 -*-
# @Time    : 2018/12/11 14:38
# @Author  : Hodge
# @Desc:

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(numbers):
            num_need = target - num
            if num_need < num or num_need > numbers[len(numbers)-1] or num_need not in numbers[i + 1:]:
                continue
            site = numbers[i + 1:].index(num_need)
            return [i + 1, site + i + 2]


list_test = [0, 0, 11, 17]
sl = Solution()
print(sl.twoSum(list_test, 0))
