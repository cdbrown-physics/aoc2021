import logging
import argparse
import sys
import numpy as np
from shutil import copyfile


def CalcGammaRate(args):
    numberOfBits = None
    numberOfLines = 0
    bitList = []
    bitString = '0b'
    with open(args.path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if numberOfBits == None:
                numberOfBits = len(line)
                bitList = np.zeros(numberOfBits)
            for b in range(numberOfBits):
                bitList[b] += int(line[b])
            numberOfLines += 1
    bitList = [1 if b > numberOfLines/2 else 0 for b in bitList]
    for b in bitList:
        bitString = bitString + str(b)
    return bitString

def CalcEpsilonRate(gammaRate):
    gammaRate = gammaRate[2:]
    print(gammaRate)
    bitString = "0b"
    epsilonRate = [int(not int(b)) for b in gammaRate]
    for b in epsilonRate:
        bitString = bitString + str(b)
    return bitString

def PartOne(args):
    gammaRate   = None
    epsilonRate = None
    gammaRate = CalcGammaRate(args)
    print("The gamma rate is", gammaRate, int(gammaRate, 2))
    epsilonRate = CalcEpsilonRate(gammaRate)
    print("The epsilon rate is", epsilonRate, int(epsilonRate, 2))
    print("The answer to part one is", int(gammaRate, 2) * int(epsilonRate, 2) )

def CalcO2Rating(args):
    """
    Find the most common bit in the position, then eliminate all numbers that
    don't have that value. repeate until on one number remains
    """
    reportList = []
    with open(args.path, 'r') as file:
        for line in file:
            reportList.append(line.strip('\n'))
    while len(reportList) > 1:
        for b in range(len(reportList[0])):
            bitCount = 0
            for line in reportList:
                bitCount += int(line[b])
            print(bitCount, len(reportList))
            if bitCount >= len(reportList)/2:
                reportList = [line for line in reportList if line[b] == '1']
            else:
                reportList = [line for line in reportList if line[b] == '0']
            if len(reportList) == 1:
                break
    O2String = '0b' + reportList[0]
    return O2String
            

def CalcCO2Rating(args, ):
    reportList = []
    with open(args.path, 'r') as file:
        for line in file:
            reportList.append(line.strip('\n'))
    while len(reportList) > 1:
        for b in range(len(reportList[0])):
            bitCount = 0
            for line in reportList:
                bitCount += int(line[b])
            print(bitCount, len(reportList))
            if bitCount >= len(reportList)/2:
                reportList = [line for line in reportList if line[b] == '0']
            else:
                reportList = [line for line in reportList if line[b] == '1']
            if len(reportList) == 1:
                break
    CO2String = '0b' + reportList[0]
    return CO2String

def PartTwo(args):
    O2Rate  = None
    CO2Rate = None
    O2Rate = CalcO2Rating(args)
    print("The O2 rate is", O2Rate, int(O2Rate, 2))
    CO2Rate = CalcCO2Rating(args)
    print("The CO2 rate is", CO2Rate, int(CO2Rate, 2))
    print("The Answer to part two is", int(O2Rate, 2) * int(CO2Rate, 2))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    args = parser.parse_args()

    PartOne(args)
    PartTwo(args)