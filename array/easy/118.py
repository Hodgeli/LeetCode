# -*- coding:utf-8 -*-
# @Time    : 2018/11/26 16:48
# @Author  : Hodge
# @Desc:
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            list_result = [[1]]
            for i in range(1,numRows):
                last_row = list_result[i-1]
                list_row = [1]
                for i in range(0,len(last_row)-1):
                    list_row.append(last_row[i]+last_row[i+1])
                list_row.append(1)
                list_result.append(list_row)

            return list_result


arr = raw_input()
num = int(arr.split()[0])
print(num)
sl = Solution()
print(sl.generate(num))