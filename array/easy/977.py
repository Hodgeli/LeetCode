# -*- coding:utf-8 -*-
# @Time    : 2019/3/13 15:50
# @Author  : Hodge
# @Desc:

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        list_minus = []
        list_posi = []
        for i in A:
            if i < 0:
                list_minus.append(i * i)
            else:
                list_posi.append(i * i)

        list_minus.reverse()

        list_result = []
        len_posi = len(list_posi)
        len_minus = len(list_minus)

        i, j = 0, 0
        while i < len_minus and j < len_posi:
            if list_minus[i] < list_posi[j]:
                list_result.append(list_minus[i])
                i += 1
            else:
                list_result.append(list_posi[j])
                j += 1

        if i < len_minus:
            list_result += list_minus[i:len_minus]
        else:
            list_result += list_posi[j:len_posi]

        return list_result


candidates = [-1,2,2]
tester = Solution()
print(tester.sortedSquares(candidates))
