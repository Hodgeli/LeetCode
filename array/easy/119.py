# -*- coding:utf-8 -*-
# @Time    : 2018/11/27 9:31
# @Author  : Hodge
# @Desc:

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            list_seed = [1]
            for i in range(rowIndex):
                list_result = [1]
                for j in range(len(list_seed) - 1):
                    list_result.append(list_seed[j] + list_seed[j + 1])
                list_result.append(1)
                list_seed = list_result
            return list_result


arr = raw_input()
num = int(arr.split()[0])
print(num)
sl = Solution()
print(sl.getRow(num))
