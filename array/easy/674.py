# -*- coding:utf-8 -*-
# @Time    : 2018/12/20 11:08
# @Author  : Hodge
# @Desc:

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                result = max(count+1,result)
                count = 0
        result = max(count+1,result)
        return result



A = [1,3,5,7]
sl = Solution()
print(sl.findLengthOfLCIS(A))
