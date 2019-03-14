# -*- coding:utf-8 -*-
# @Time    : 2019/3/14 21:07
# @Author  : Hodge
# @Desc:

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        list_K = []
        while K:
            list_K.append(K % 10)
            K //= 10
        list_K.reverse()
        len_A = len(A)
        len_K = len(list_K)

        if len_A < len_K:
            temp = len_K
            len_K = len_A
            len_A = temp
            temp = A
            A = list_K
            list_K = temp

        is_carry = 0
        while len_K:
            temp = A[len_A - 1] + list_K[len_K - 1] + is_carry
            if temp > 9:
                A[len_A - 1] = temp % 10
                is_carry = 1
            else:
                A[len_A - 1] = temp
                is_carry = 0
            len_A -= 1
            len_K -= 1
        while is_carry:
            if len_A - 1 < 0:
                A = [1] + A
                break
            else:
                temp = A[len_A - 1] + 1
                if temp > 9:
                    A[len_A - 1] = temp % 10
                    is_carry = 1
                else:
                    A[len_A - 1] = temp
                    is_carry = 0
            len_A -= 1
        return A


list_test = [1,2,3,4]
tester = Solution()
print(tester.addToArrayForm(list_test, 8766))
