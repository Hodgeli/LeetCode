# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 15:24
# @Author  : Hodge
# @Desc:

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        list_result = []
        count = 0
        for seat in seats:
            if seat == 0:
                count += 1
            else:
                list_result.append(count)
                count = 0
        list_result.append(count)
        max_one = max(list_result)
        if max_one % 2 == 0:
            max_one = max_one / 2
        else:
            max_one = max_one / 2 + 1
        max_two = list_result[0]
        max_three = list_result[-1]
        return max(max_one, max_two, max_three)


A = [1, 0, 0, 0, 1, 0, 1]
sl = Solution()
print(sl.maxDistToClosest(A))
