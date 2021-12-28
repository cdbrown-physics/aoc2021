import logging
import argparse
import sys
import numpy as np
import re

def RangeSum(steps):
    return sum(range(1, steps + 1))

def PartOne(args):
    with open(args.path, 'r') as file:
        for line in file:
            crabList = re.findall("[0-9]+", line) # Should only be one line
        crabList = [int(c) for c in crabList]
    minimumCrabStart = min(crabList)
    maximumCrabStart = max(crabList)
    logging.info("Crab range is {} {}".format(minimumCrabStart, maximumCrabStart))
    fuelUsed = []
    for endPoint in range(minimumCrabStart, maximumCrabStart):
        fooFuel = 0
        for crab in crabList:
            fooFuel += abs(crab - endPoint)
        fuelUsed.append(fooFuel)
    # Now find the minimum fule
    minFuleUsed = min(fuelUsed)
    print("Minimum fuel used is {}".format(minFuleUsed))

def PartTwo(args):
    with open(args.path, 'r') as file:
        for line in file:
            crabList = re.findall("[0-9]+", line) # Should only be one line
        crabList = [int(c) for c in crabList]
    minimumCrabStart = min(crabList)
    maximumCrabStart = max(crabList)
    logging.info("Crab range is {} {}".format(minimumCrabStart, maximumCrabStart))
    fuelUsed = []
    for endPoint in range(minimumCrabStart, maximumCrabStart):
        fooFuel = 0
        for crab in crabList:
            fooFuel += RangeSum(abs(crab - endPoint))
        fuelUsed.append(fooFuel)
    # Now find the minimum fule
    minFuelUsed = min(fuelUsed)
    print("Minimum fuel used is {}".format(minFuelUsed))          
            
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    parser.add_argument("--days", help="How many days you want to run", type=int)
    args = parser.parse_args()
    
    logging.basicConfig(level=args.dl)
    PartOne(args)
    PartTwo(args)