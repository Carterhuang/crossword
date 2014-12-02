vowels = ['a', 'e', 'i', 'o', 'u']

"""
    This function returns true if the word does match the pattern.
    For example, the word "make" matches "_a_e" and therefore it 
    returns true.
"""
def match(pattern, w):
    len1, len2 = len(pattern), len(w)
    if (len1 != len2):
        return False
    for i in xrange(len1):
        if pattern[i] != '_' and pattern[i] != w[i]:
            return False
    return True

"""
    With direction 0, this subroutine fills the board horizontally 
    while with direction 1 vertically.
"""
def fillBoard(board, x, y, w, direction):
    if direction == 0:
        # Fill horizontally.
        for i in xrange(len(w)):
            try:
                board[x][y+i] = w[i]
            except IndexError:
                print 'Index Error\nx: %d, y: %d'%(x, y+i)
                sys.exit(1)
    elif direction == 1:
        # Fill vertically.
        for i in xrange(len(w)):
            try:
                board[x+i][y] = w[i]
            except IndexError:
                print 'Index Error\nx: %d, y: %d'%(x+i, y)
                sys.exit(2)
    else:
        print 'Invalid direction'
        sys.exit(3)

def constructMatchPatterns(board, x, y, direction):
    # Constructing matching keys.
    N, M = len(board), len(board[0])
    key, match_key = '', ''
    start = y

    if direction == 0:
        while y < M and board[x][y] != '.':
            if board[x][y] not in vowels:
                key += '_'
            else:
                key += board[x][y]
            match_key += board[x][y]
            y += 1
    if direction == 1:
        while x < N and board[x][y] != '.':
            if board[x][y] not in vowels:
                key += '_'
            else:
                key += board[x][y]
            match_key += board[x][y]
            x += 1
    return key, match_key

"""
    A boolean function that returns true if space is found
    in a row or column.
"""
def searchSpace(board, x, y, direction):
    N, M = len(board), len(board[0])

    if direction == 0:
        # Scan horizontally.
        while y > 0 and board[x][y-1] != '.':
            y -= 1
        while y < M and board[x][y] != '.':
            if board[x][y] == '_':
                return True
            y += 1
        return False
    elif direction == 1:
        # Scan vertically.
        while x > 0 and board[x-1][y] != '.':
            x -= 1
        if board[x][y] == '.': x += 1
        while x < N and board[x][y] != '.':
            if board[x][y] == '_':
                return True
            x += 1
        return False
    return False

"""
    Search the board to see if there is any opening
    left.
"""
def searchBoard(board):
    N, M = len(board), len(board[0])
    for i in xrange(N):
        for j in xrange(M):
            if board[i][j] == '_':
                return i, j
    return -1, -1

def toWordPattern(word):
    missingword = ''
    for w in word:
        w = '_' if w not in vowels else w
        missingword += w
    return missingword

"""
    Tested, safe find missing words function.
"""
def findMissingWords(board):
    missing = []
    word = ''
    N, M = len(board), len(board[0])
    # Scan rows.        
    for i in xrange(N):
        for j in xrange(M):
            if board[i][j] != '.':
                word += board[i][j]
            else: # Encounter '.'
                if len(word) > 1:
                    missing.append(word)
                word = ''

        if len(word) > 1:
            missing.append(word)
        word = ''
    # Scan colomns.
    for j in xrange(M):
        for i in xrange(N):
            if board[i][j] != '.':
                word += board[i][j]
            else: # Encounter '.'
                if len(word) > 1:
                    missing.append(word)
                word = ''

        if len(word) > 1:
            missing.append(word)
        word = ''
    return missing

def buildDict(corpus, missings):
    my_dict = {}
    for m in missings:
        my_dict[m] = []

    with open(corpus, 'r') as corp:
        words = corp.read().split('\n')
        words.pop()

        for word in words:
            key = toWordPattern(word)
            if key in my_dict:
                my_dict[key].append(word)
    return my_dict
