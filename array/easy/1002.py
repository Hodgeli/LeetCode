# -*- coding:utf-8 -*-
# @Time    : 2019/3/14 19:23
# @Author  : Hodge
# @Desc:

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        for i in A[0]:
            result.append(i)

        for item in A[1:]:
            list_temp = []
            for i in item:
                if i in result:
                    list_temp.append(i)
                    result.remove(i)
            result = list_temp
        return result

list_test = ["cool","lock","cook"]
tester = Solution()
print(tester.commonChars(list_test))
