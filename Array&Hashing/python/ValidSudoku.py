"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
##
from collections import defaultdict
board = [["5","5",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["7",".",".","8",".","3",".",".","1"]
        ,["9",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","5","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = defaultdict(list)
sqr = defaultdict(list)
col = defaultdict(list)

class Solution:
    def ValidSudoku():
        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num =='.':
                    continue 
                
                if (num in row[r] or num in col[c] or num in sqr[(r//3, c//3)]):
                    return False
                else:
                    row[r].append(num)
                    col[c].append(num)
                    sqr[(r//3, c//3)].append(num)
        return True        
