import logging
import argparse
import sys
import numpy as np
import re
from shutil import copyfile

class Board:
    def __init__(self):
        # Need to make a board
        pass

def ParseInput(path):
    # Fuck this input
    bingoNumers = []
    boards = []
    board = []
    with open(path, 'r') as file:
        for line in file:
            # First line is always the bingo numbers
            if len(bingoNumers) == 0:
                line = re.findall('[0-9]+', line)
                bingoNumers = [int(i) for i in line]
            elif len(line.strip('\n')) > 0: # Want to skip lines that are just new lines
                boardLine = re.findall('[0-9]+', line)
                boardLine = [int(i) for i in boardLine]
                board.append(boardLine)
                if len(board) >= 5:
                    # print(board)
                    boards.append(np.array(board))
                    board = []
    return boards, bingoNumers

def FindBingoBoard(boards, bingoNumbers):
    # Finds the first bingo
    """
    Marks a hit by turning the number to -1
    """
    for bingoNumber in bingoNumbers:
        for board in boards:
            if bingoNumber in board:
                logging.debug("bingo number {} is in board\n {}".format(bingoNumber, board))
                logging.debug("At location {}".format(np.where(board==bingoNumber)))
                location = np.where(board==bingoNumber)
                board[location] = -1
                row = board[location[0], :][0]
                col = [i for k in board[:, location[1]] for i in k]
                # After each hit check to see if we have a bingo or not. Only
                # need to look in that row and column that you have. 
                logging.debug("the row were the number was found {}".format(row))
                logging.debug("the column of numbers found is".format(col))
                if all(i == -1 for i in row) or all(i == -1 for i in col):
                    print("bingo found in board", board)
                    return board, bingoNumber

def FindLastWinBoard(boards, bingoNumbers):
    lastWinBoard = 0
    lastWinNumber = 0
    for bingoNumber in bingoNumbers:
        stableBoards = boards.copy()
        for board in stableBoards:
            logging.info("Looking at board\n {}".format(board))
            logging.info("Bingo number is: {}".format(bingoNumber))
            if bingoNumber in board:
                logging.debug("bingo number {} is in board\n {}".format(bingoNumber, board))
                logging.debug("At location {}".format(np.where(board==bingoNumber)))
                location = np.where(board==bingoNumber)
                board[location] = -1
                row = board[location[0], :][0]
                col = [i for k in board[:, location[1]] for i in k]
                # After each hit check to see if we have a bingo or not. Only
                # need to look in that row and column that you have. 
                logging.debug("the row were the number was found {}".format(row))
                logging.debug("the column of numbers found is {}".format(col))
                if all(i == -1 for i in row) or all(i == -1 for i in col):
                    # Now we want to set the lastWinBoard to be the winning board
                    # but also remoe it from the boards list so we don't keep checking
                    # the same boards over and over
                    lastWinBoard = board
                    lastWinNumber = bingoNumber
                    logging.info("Winning number is {}".format(lastWinNumber))
                    logging.info("Winning board is {}".format(lastWinBoard))
                    removearray(boards, board)
    return lastWinBoard, lastWinNumber
                    
def removearray(L, arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind], arr):
        ind += 1
    if ind != size:
        L.pop(ind)
                    
def PartOne(args):
    boards, bingoNumbers = ParseInput(args.path)
    boardWin, numberWin = FindBingoBoard(boards, bingoNumbers)
    
    boardScoreList = [i for j in boardWin for i in j if i >= 0]
    boardScore = sum(boardScoreList)
    print("Board score is", boardScore)
    print("Answer to part one is", boardScore * numberWin)
    return 0
             
def PartTwo(args):
    boards, bingoNumbers = ParseInput(args.path)
    boardLose, numberWin = FindLastWinBoard(boards, bingoNumbers)
    
    boardScoreList = [i for j in boardLose for i in j if i >= 0]
    boardScore = sum(boardScoreList)
    print("Board score is", boardScore)
    print("Answer to part one is", boardScore * numberWin)
    return 0
     
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    args = parser.parse_args()
    
    logging.basicConfig(level=args.dl)

    PartOne(args)
    PartTwo(args)
        