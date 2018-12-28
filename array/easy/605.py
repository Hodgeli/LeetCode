# -*- coding:utf-8 -*-
# @Time    : 2018/12/27 16:33
# @Author  : Hodge
# @Desc:

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        max_new = 0
        nn = len(flowerbed)
        i = 0
        j = nn - 1
        for i in range(nn):
            if flowerbed[i] == 1:
                break
        if i == j and flowerbed[-1] == 0:  # all zero
            temp = nn % 2
            if temp:
                max_new += nn / 2 + 1
            else:
                max_new += nn / 2
        else:
            for j in range(nn - 1, -1, -1):
                if flowerbed[j] == 1 or j == i:
                    break
            if j == i:  # only one one
                max_new += i / 2 + (nn - j - 1) / 2
            else:  # three part
                max_new += i / 2 + (nn - j - 1) / 2
                flowerbed = flowerbed[i:j + 1]
                temp = 0
                list_zero = []
                for item in flowerbed:
                    if item == 0:
                        temp += 1
                    elif item == 1 and temp != 0:
                        list_zero.append(temp)
                        temp = 0
                if temp != 0:
                    list_zero.append(temp)
                for item in list_zero:
                    max_new += (item - 1) / 2

        # print(max_new)
        if max_new >= n:
            return True
        else:
            return False


list_test = [0,0,0,0,1]
sl = Solution()
print(sl.canPlaceFlowers(list_test, 1))
