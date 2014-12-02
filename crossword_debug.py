from crossword import *
from copy import deepcopy

def printBoard(board):
    for l in board:
        print ' '.join(l)

board = [['.', '_', '_', 'a', '_', '.', '.', '_'],
         ['.', 'o', '.', '.', 'u', '.', '.', 'o'],
         ['e', '_', '_', '.', '_', '_', 'o', '_'],
         ['.', '_', '.', '_', '.', 'a', '.', '.'],
         ['.', '.', '_', 'a', '_', '_', '.', '.'],
         ['.', '_', 'i', '_', '.', '_', 'a', '_'],
         ['_', 'o', '_', '_', 'e', '.', '.', 'o'],
         ['o', '.', '.', '.', '_', '.', '.', 'a'],
         ['_', 'o', 'o', '_', 'e', '.', '.', '_']]

printBoard(board)
solver = CrosswordSolver(board)

print '\nTest find missing'
missings = findMissingWords(board)
print missings

print '\nTest searchspace'
print searchSpace(board, 2, 7, 0)
print searchSpace(board, 2, 7, 1)
print searchSpace(board, 2, 0, 0)
print searchSpace(board, 2, 0, 1)
print searchSpace(board, 4, 0, 0)


print '\nTest construct missing'
print constructMatchPatterns(board, 0, 1, 0)
print constructMatchPatterns(board, 0, 1, 1)
print match('__o_', 'plow')

board_cp = deepcopy(board)

print '\nTest fill function'
fillBoard(board_cp, 0, 1, 'plow', 0)
fillBoard(board_cp, 0, 7, 'cow', 1)
printBoard(board_cp)

print '\nTest dictionary construction function'
dic = buildDict('corpus', missings)
for k in dic:
    print k, len(dic[k])

print '\nTest solving algorithm'
printBoard(solver.solve())

















