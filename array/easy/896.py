# -*- coding:utf-8 -*-
# @Time    : 2018/12/4 9:45
# @Author  : Hodge
# @Desc:

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        else:
            result = A[0] - A[1]
            for i in range(1, len(A) - 1):
                temp = A[i] - A[i + 1]
                if result * temp < 0:
                    return False
                if temp != 0:
                    result = temp
            return True


list_test = [2, 2, 2, 1, 4, 5]
sl = Solution()
print(sl.isMonotonic(list_test))
