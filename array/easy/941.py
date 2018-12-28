# -*- coding:utf-8 -*-
# @Time    : 2018/12/26 17:17
# @Author  : Hodge
# @Desc:

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3 or A[0] > A[1]:
            return False
        else:
            flag = 0
            for i in range(1, n):
                if flag == 0:
                    if A[i - 1] > A[i]:
                        flag = 1
                    elif A[i - 1] == A[i]:
                        return False
                else:
                    if A[i - 1] <= A[i]:
                        return False
            if flag == 0:
                return False
            else:
                if A[n - 1] > A[n - 2]:
                    return False
                return True


A = [9,8,7,6,5,4,3,2,1,0]
sl = Solution()
print(sl.validMountainArray(A))
