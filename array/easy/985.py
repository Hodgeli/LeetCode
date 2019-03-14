# -*- coding:utf-8 -*-
# @Time    : 2019/3/14 11:15
# @Author  : Hodge
# @Desc:

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = [0]
        index_answer = 0
        for i in A:
            if i % 2 == 0:
                answer[0] += i

        for item in queries:
            val = item[0]
            index = item[1]
            # A_val = A[index]
            index_answer += 1
            answer.append(0)
            if val % 2 == 0:
                if A[index] % 2 == 0:
                    answer[index_answer] = answer[index_answer-1] + val
                else:
                    answer[index_answer] = answer[index_answer-1]
            else:
                if A[index] % 2 == 0:
                    answer[index_answer] = answer[index_answer-1] - A[index]
                else:
                    answer[index_answer] = answer[index_answer-1] + (A[index]+val)
            A[index] += val
        return answer[1:]


A = [3,2]
queries = [[4,0],[3,0]]
tester = Solution()
print(tester.sumEvenAfterQueries(A, queries))
