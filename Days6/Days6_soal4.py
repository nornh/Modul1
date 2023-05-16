def printBoard(board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('--+---+--')
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('--+---+--')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

board = {
    'top-L': 'X', 'top-M': 'O', 'top-R': ' ',
    'mid-L': 'O', 'mid-M': 'X', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

printBoard(board)
