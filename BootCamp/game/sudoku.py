# board
# sufficient numbers4
# unique numbers in row and cols
# 4 --> 2
# 9 --> 3
import math
import numpy as np

board = int(input("what size do you want"))
r_b = int(board**0.5)

if type(math.isqrt(board)) == int:
    sb = []
    for i in range(board):
        l1 = []
        for j in range(board):
            l1.append(0)
        sb.append(l1)
        del(l1)

p = sb


def user_ip():
    row = int(input("what row you want to play: "))
    col = int(input("what col you want to play: "))

    num = int(input("Enter Number: "))
    # block max limit==board/2
    # checker while input
    # 30% of round(board**2)

    return row, col, num


limit = round(board**2 * 0.3)


def checker(row, col, num):
    '''
    to check if thhe number repeats in a 

    block, 
    row and
    column
    '''
    r_counter = 0
    for i in range(board):
        if p[row][i] == num:
            r_counter += 1

    c_counter = 0
    for i in range(board):
        if p[i][col] == num:
            c_counter += 1

    if c_counter == 1 and r_counter == 1:
        return True
    else:
        print('entered number already exists ')
        p[row][col] = 0
        return False


def usblock(num):
    pre_row = row - row % r_b
    post_row = row - (row % r_b) + r_b
    pre_col = col - col % r_b
    post_col = col - (col % r_b) + r_b
    count = 0
    for i in range(pre_row, post_row):
        for j in range(pre_col, post_col):
            pos = p[i][j]
            if pos == num:
                count += 1
    if count > 1:
        print("Num repeated enter new number!!")
        p[row][col] = 0
    elif count == 1:
        return True


def find_empty(bo):
    for i in range(0, board):
        for j in range(0, board):
            if bo[i][j] == 0:
                return (i, j)
    return None


def solver(bo):
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

        for i in range(0, board):
            if checker(row, col, i) & usblock(i):
                bo[row][col] = i

                if solver(bo):
                    return True

                bo[row][col] = 0
    return False


bar = 0
while bar <= limit:
    row, col, num = user_ip()
    p[row][col] = num
    if checker(row, col, num):
        if usblock(num):
            sb[row][col] = num
            print(f'chal gaya...{num}')
            print(sb)
            bar += 1
        else:
            print('error occ.')

print(sb)

print('*'*30)
solver(sb)

print(sb)
