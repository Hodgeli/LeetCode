# -*- coding:utf-8 -*-
# @Time    : 2018/12/20 11:13
# @Author  : Hodge
# @Desc:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        count = 0
        for num in digits:
            count += num * pow(10, n)
            n -= 1
        count += 1
        result = []
        while(count):
            result.append(count%10)
            count /= 10
        return result[::-1]


A = [1, 3, 5, 7]
sl = Solution()
print(sl.plusOne(A))
