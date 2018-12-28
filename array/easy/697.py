# -*- coding:utf-8 -*-
# @Time    : 2018/12/11 16:52
# @Author  : Hodge
# @Desc:
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_num_times = {}
        dict_num_start_end = {}
        result = 0
        degree = 0
        for i, num in enumerate(nums):
            if num not in dict_num_times:
                dict_num_times[num] = 1
                dict_num_start_end[num] = [i, i]
            else:
                dict_num_times[num] += 1
                dict_num_start_end[num][1] = i
            if dict_num_times[num] == degree:
                temp_du = dict_num_start_end[num][1] - dict_num_start_end[num][0] + 1
                if temp_du < result:
                    result = temp_du
            elif dict_num_times[num] > degree:
                result = dict_num_start_end[num][1] - dict_num_start_end[num][0] + 1
                degree = dict_num_times[num]

        return result


A = [1, 2, 2, 3, 1, 4, 2]
sl = Solution()
print(sl.findShortestSubArray(A))
