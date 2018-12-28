# -*- coding:utf-8 -*-
# @Time    : 2018/12/17 9:22
# @Author  : Hodge
# @Desc:

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        while i < n:
            if bits[i] == 0:
                i += 1
                if i >= n:
                    return True
            else:
                i += 2
                if i >= n:
                    return False


A = [1, 1, 1, 0]
sl = Solution()
print(sl.isOneBitCharacter(A))
