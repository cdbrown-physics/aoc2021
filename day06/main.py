import logging
import argparse
import sys
import numpy as np
import re

def GetInput(path):
    """ 
    This problem should only have one line input
    Returns a numpy array
    """
    with open(path, 'r') as file:
        for line in file:
            fishList = re.findall("[0-9]+", line)
            print(fishList)
    fishList = [int(i) for i in fishList]
    fishList = np.array(fishList)
    return fishList

def PartOne(args):
    
    fishInput = GetInput(args.path)
    day = 0
    while True:
        logging.debug("After day {}: {}".format(day, fishInput))
        if day >= args.days:
            break 
        fishInput -= 1
        for f in range(len(fishInput)):
            if fishInput[f] < 0:
                fishInput[f] = 6
                fishInput = np.append(fishInput, 8)
        day += 1
        logging.info("Finishing day {}".format(day))
    print("After {} days there are {} fish".format(args.days, len(fishInput)))
        

def PartTwo(args):
    fishInput = GetInput(args.path) 
    fishDict = {"0": 0, "1": 0, "2": 0,
                "3": 0, "4": 0, "5": 0,
                "6": 0, '7': 0, '8': 0}
    # Turn the array into a dictionary, and just found how many fish are in each day?
    for f in range(9):
        fishCount = np.count_nonzero(fishInput == f)
        fishDict[str(f)] = fishCount
    # Now you just need to move the numbers down to a the next element and we 
    # should be good, add 6 and 8 when needed
    print(fishDict)
    day = 0
    while True:
        fooFish = fishDict.copy()
        if day >= args.days:
            break
        for key in fooFish:
            logging.debug("Lookin in key {}".format(key))
            if int(key) == 0:
                nextKey = "6"
                logging.debug("Laying {} eggs".format(fooFish[key]))
                fishDict["8"] = fooFish[key]
                fishDict[nextKey] = fooFish[key]
            elif key == '7':
                nextKey = str(int(key) - 1)
                fishDict[nextKey] += fooFish[key]
            else:
                nextKey = str(int(key) - 1)
                fishDict[nextKey] = fooFish[key]
        day += 1
        logging.debug(fishDict)
        logging.info("Finishing day {}".format(day))
    answer = 0
    for f in fishDict.values():
        answer += f
    print("After {} days there are {} fish".format(args.days, answer))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    parser.add_argument("--days", help="How many days you want to run", type=int)
    args = parser.parse_args()
    
    logging.basicConfig(level=args.dl)
    # PartOne(args)
    PartTwo(args)