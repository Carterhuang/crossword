from copy import deepcopy
from utility import *
import sys

def printBoard(board):
    for l in board:
        print ' '.join(l)

"""
    This class contains the main logic for the algorithm:
    both words grouping as well as backtracking.
"""
class CrosswordSolver:

    def __init__(self, board=[[]], corpus='corpus'):
        if board == [[]]:
            return 
        self.loadBoard(board, corpus)

    def loadBoard(self, board, corpus='corpus'):
        print 'Here is the puzzle:'
        printBoard(board)
        print 'Solving ...'
        self.board = deepcopy(board)
        global N , M
        N = len(board)
        M = len(board[0])
        #print N, M
        self.T_map = [[0 for i in xrange(M)] for j in xrange(N)]
        for i in xrange(N):
            for j in xrange(M):
                if board[i][j] == '.':
                    self.T_map[i][j] = 0
                else:
                    self.T_map[i][j] = 1

        self.missings = findMissingWords(self.board)
        self.dictionary = buildDict(corpus, self.missings)
 
    def guessRow(self, x, y):
        cross, board, T_map = 0, self.board, self.T_map

        # Shift pointer to the leftmost position.
        while y > 0 and board[x][y-1] != '.':
            y -= 1
            cross += 1
        start = y           

        y, next_guess = start, []

        # Update position on the T_map and figure out where to 
        # to go for next guesses.
        while y < M and T_map[x][y] != 0:
            up = x > 0 and T_map[x-1][y] != 0
            down = x < N-1 and T_map[x+1][y] != 0
            not_traversed = searchSpace(board, x, y, 1)
            if not_traversed and (up or down):
                next_guess.append((x, y))
            T_map[x][y] += 1            
            y += 1

        y = start

        key, match_key = constructMatchPatterns(board, x, start, 0)
        try: 
            sub_dictionary = self.dictionary[key]
        except:
            return False

        for w in sub_dictionary:
            if match(match_key, w):
                fillBoard(board, x, y, w, 0) 
                is_match = True
                for n in next_guess:
                    if not self.guessCol(n[0], n[1]):
                        is_match = False
                        break
                # Successfully traversed everything.
                if is_match:
                    return 1
        fillBoard(board, x, y, match_key, 0)
        return 0
        
    def guessCol(self, x, y):
        cross, board, T_map = 0, self.board, self.T_map
        
        # Shift pointer to the leftmost position.
        while x > 0 and board[x-1][y] != '.':
            x -= 1
            cross += 1
        start = x           
 
        x, next_guess = start, []

        # Update position on the T_map and figure out where to 
        # to go for next guesses.
        while x < N and T_map[x][y] != 0:
            left = y > 0 and T_map[x][y-1] != 0
            right = y < M-1 and T_map[x][y+1] != 0
            not_traversed = searchSpace(board, x, y, 0)
            if (left or right) and not_traversed:
                next_guess.append((x, y))
            T_map[x][y] += 1            
            x += 1
        x = start
        key, match_key = constructMatchPatterns(board, start, y, 1)

        try: 
            sub_dictionary = self.dictionary[key]
        except:
            return False

        for w in sub_dictionary:
            if match(match_key, w):
                fillBoard(board, x, y, w, 1) 
                is_match = True
                for n in next_guess:
                    if not self.guessRow(n[0], n[1]):
                        is_match = False
                        break
                # Successfully traversed everything.
                if is_match:
                    return 1
        fillBoard(board, x, y, match_key, 1)
        return 0

    """
        Keep searching the board for openings, If there is one,
        then that means a word needs to be filled there.
    """
    def solve(self):
        board = self.board
        x, y = searchBoard(board)
        while x != -1:
            if (not self.guessRow(x, y)) and (not self.guessCol(x, y)):
                print 'Failed to Solve.'
                return board
            x, y = searchBoard(board)
        print 'Solved.'
        return board 
    




