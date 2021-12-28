import logging
import argparse
import sys
import numpy as np
import re

def BiRange(start, stop):
    if start <= stop:
        return np.arange(start, stop+1)
    elif start > stop:
        return np.arange(start, stop-1, -1)
    else:
        sys.exit("Invalid inputs to BiRange. {} {}".format(start, stop))

def GetDiagonal(x1, y1, x2, y2):
    coordinates = []
    if x1 < x2:
        logging.debug("x1 < x2")
        xList = np.arange(x1, x2 + 1)
    else:
        logging.debug("x1 > x2")
        xList = np.arange(x1, x2-1, -1)
    if y1 < y2:
        logging.debug("y1 < y2")
        yList = np.arange(y1, y2+1)
    else:
        logging.debug("y1 > y2")
        yList = np.arange(y1, y2-1, -1)
    for x, y in zip(xList, yList):
        coordinates.append([x,y])
    logging.debug(xList)
    logging.debug(yList)
    logging.debug(coordinates)
    return coordinates

def PartOne(args):
    ventDictionary = {}
    totalOverlap = 0
    with open(args.path, 'r') as file:
        for line in file:
            x1, y1, x2, y2 = re.findall("[0-9]+", line)
            logging.debug("{} {} {} {}".format(x1, y1, x2, y2))
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            if x1 == x2:
                # Then the line is vertical
                logging.info("vertical line")
                for y in BiRange(y1, y2):
                    keyString = "{},{}".format(x1, y)
                    if keyString in ventDictionary:
                        ventDictionary[keyString] += 1
                    else:
                        ventDictionary[keyString] = 1
            elif y1 == y2:
                # The line is horixontal
                logging.info("horizontal line")
                for x in BiRange(x1, x2):
                    keyString = "{},{}".format(x, y1)
                    if keyString in ventDictionary:
                        ventDictionary[keyString] += 1
                    else:
                        ventDictionary[keyString] = 1
            else:
                logging.info("line is neither horizontal or vertical")
    
    logging.debug(ventDictionary)
    # Now that we've mapped out all of these vent paths. 
    for i in ventDictionary.values():    
        if i >= 2:
            totalOverlap += 1
    print("Answer to part one", totalOverlap)
            
            
def PartTwo(args):
    ventDictionary = {}
    totalOverlap = 0
    with open(args.path, 'r') as file:
        for line in file:
            x1, y1, x2, y2 = re.findall("[0-9]+", line)
            logging.debug("{} {} {} {}".format(x1, y1, x2, y2))
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            if x1 == x2:
                # Then the line is vertical
                logging.info("vertical line")
                for y in BiRange(y1, y2):
                    keyString = "{},{}".format(x1, y)
                    if keyString in ventDictionary:
                        ventDictionary[keyString] += 1
                    else:
                        ventDictionary[keyString] = 1
            elif y1 == y2:
                # The line is horixontal
                logging.info("horizontal line")
                for x in BiRange(x1, x2):
                    keyString = "{},{}".format(x, y1)
                    if keyString in ventDictionary:
                        ventDictionary[keyString] += 1
                    else:
                        ventDictionary[keyString] = 1
            else:
                diagonalList = GetDiagonal(x1,y1,x2,y2)
                logging.info("diagonal line")
                for x, y in diagonalList:
                    keyString="{},{}".format(x, y)
                    if keyString in ventDictionary:
                        ventDictionary[keyString] += 1
                    else:
                        ventDictionary[keyString] = 1
    
    logging.debug(ventDictionary)
    # Now that we've mapped out all of these vent paths. 
    for i in ventDictionary.values():    
        if i >= 2:
            totalOverlap += 1
    PrintGrid(ventDictionary)
    print("Answer to part two", totalOverlap)
    
def PrintGrid(grid):
    stringPrint = ''
    for y in range(1000):
        for x in range(1000):
            keyString = "{},{}".format(x, y)
            if keyString in grid:
                stringPrint += '{}'.format(grid[keyString])
            else:
                stringPrint += '.'
        print(stringPrint)
        stringPrint = ''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    args = parser.parse_args()
    
    logging.basicConfig(level=args.dl)
    #PartOne(args)
    #GetDiagonal(1, 1, 3, 3)
    #GetDiagonal(9,7,7,9)
    #GetDiagonal(8,0,0,8)
    #GetDiagonal(0,0,8,8)
    PartTwo(args)
    