# -*- coding:utf-8 -*-
# @Time    : 2018/11/27 10:34
# @Author  : Hodge
# @Desc:
import random


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        flag = 0
        for item in nums:
            if item ==1:
                flag += 1
            else:
                if flag > max:
                    max = flag
                flag = 0
        if flag > max:
            max = flag
        return max


A = []
seed = [0, 1]
for i in range(20):
    A.append(random.choice(seed))

print(A)

sl = Solution()
print(sl.findMaxConsecutiveOnes(A))