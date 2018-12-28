# -*- coding:utf-8 -*-
# @Time    : 2018/12/18 9:42
# @Author  : Hodge
# @Desc:

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        sum = 0
        result = []
        temp = []
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                sum += 1
                if sum == 1:
                    temp = [i,i]
                else:
                    temp[1] = i
            else:
                if sum >= 2:
                    temp[1] += 1
                    result.append(temp)
                sum = 0
                temp = []
        if sum >= 2:
            temp[1] += 1
            result.append(temp)
        return result



A = "aaa"
sl = Solution()
print(sl.largeGroupPositions(A))