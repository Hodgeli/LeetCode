# -*- coding:utf-8 -*-
# @Time    : 2019/3/14 15:36
# @Author  : Hodge
# @Desc:

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        R_i = 0
        R_j = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    R_i = i
                    R_j = j

        start_i = R_i + 1
        while start_i < 8:
            if board[start_i][R_j] != '.':
                if board[start_i][R_j] == 'p':
                    result += 1
                break
            start_i += 1

        start_i = R_i - 1
        while start_i >= 0:
            if board[start_i][R_j] != '.':
                if board[start_i][R_j] == 'p':
                    result += 1
                break
            start_i -= 1

        start_j = R_j + 1
        while start_j < 8:
            if board[R_i][start_j] != '.':
                if board[R_i][start_j] == 'p':
                    result += 1
                break
            start_j += 1

        start_j = R_j - 1
        while start_j >= 0:
            if board[R_i][start_j] != '.':
                if board[R_i][start_j] == 'p':
                    result += 1
                break
            start_j -= 1

        return result


board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
tester = Solution()
print(tester.numRookCaptures(board))
