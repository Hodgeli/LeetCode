# -*- coding:utf-8 -*-
# @Time    : 2018/12/11 14:01
# @Author  : Hodge
# @Desc:

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        list_result = []
        for i in range(row):
            list_result_row = []
            for j in range(col):
                num = 0
                sum = 0
                for ii in range(i - 1, i + 2):
                    if ii < 0 or ii >= row:
                        continue
                    for jj in range(j - 1, j + 2):
                        if jj < 0 or jj >= col:
                            continue
                        sum += M[ii][jj]
                        num += 1
                list_result_row.append(sum / num)
            list_result.append(list_result_row)
        return list_result


list_test = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
sl = Solution()
print(sl.imageSmoother(list_test))
