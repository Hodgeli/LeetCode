# -*- coding:utf-8 -*-
# @Time    : 2018/12/27 15:14
# @Author  : Hodge
# @Desc:

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dict_deck = {}
        for num in deck:
            if num not in dict_deck:
                dict_deck[num] = 1
            else:
                dict_deck[num] += 1
        min_times = dict_deck[min(dict_deck, key=dict_deck.get)]
        if min_times == 1:
            return False
        else:
            flag = 0
            for i in range(2, min_times + 1):
                for item in dict_deck:
                    if dict_deck[item] % i != 0:
                        flag = 1
                        break
                if flag == 0:
                    return True
                else:
                    flag = 0
            return False


list_test = [1, 1, 1, 2, 2, 2, 3, 3]
sl = Solution()
print(sl.hasGroupsSizeX(list_test))
