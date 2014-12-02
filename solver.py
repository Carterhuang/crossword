from crossword import *
from copy import deepcopy
import sys

solver = CrosswordSolver()
test_cases = sys.argv[1:]

print 'Test cases: ', sys.argv[1:], '\n'

for f in test_cases:
    with open(f, 'r') as case:
        print '\nNow solving %s'%(f)
        rows = case.read().split('\n')
        rows.pop()
        board = [ row.split() for row in rows]
        solver.loadBoard(board)
        printBoard(solver.solve())
