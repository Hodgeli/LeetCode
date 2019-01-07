# -*- coding:utf-8 -*-
# @Time    : 2019/1/4 9:39
# @Author  : Hodge
# @Desc:牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。
# 最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。
# 现在，重复执行以下步骤，直到显示所有卡牌为止：
# 从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。
# 如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。
# 如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。
# 返回能以递增顺序显示卡牌的牌组顺序。
# 答案中的第一张牌被认为处于牌堆顶部。

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        result = [deck[-1]]
        if len(deck) == 1:
            return result
        flag = 0
        for i in range(len(deck) - 2, -1, -1):
            result.append(result[flag])
            result[flag] = 0
            result.append(deck[i])
            flag += 1
        return result[:flag - 1:-1]


test = [17]
tester = Solution()
print(tester.deckRevealedIncreasing(test))
