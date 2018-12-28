# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 16:50
# @Author  : Hodge
# @Desc:

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1 or k <= 0:
            return False

        record = set()

        for i in range(len(nums)):
            if nums[i] in record:
                return True

            record.add(nums[i])

            if len(record) >= k + 1:
                record.remove(nums[i - k])

        return False


A = [1, 2, 3, 1]
sl = Solution()
print(sl.containsNearbyDuplicate(A, 3))
