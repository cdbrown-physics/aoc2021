import logging
import argparse
import re

def getKnownNumbers(signal, numberDictionary):
    for j in signal:
        if len(j) == 2:
            numberDictionary["one"] = j
        elif len(j) == 3:
            numberDictionary["seven"] = j
        elif len(j) == 4:
            numberDictionary["four"] = j
        elif len(j) == 7:
            numberDictionary["eight"] = j
    return numberDictionary

def getFiveCount(signal):
    fiveCount = []
    for j in signal:
        if len(j) == 5:
            fiveCount.append(j)
    return fiveCount

def getSixCount(signal):
    sixCount = []
    for j in signal:
        if len(j) == 6:
            sixCount.append(j)
    return sixCount

def getMidSeg(signal):
    midSeg = []
    fiveCount = getFiveCount(signal)
    for c in fiveCount[0]:
        if c in fiveCount[1] and c in fiveCount[2]:
            # Then it's one of the middle segments
            midSeg.append(c)
    return midSeg

def getTopMid(one, seven, segdict):
    for i in seven:
        if i in one:
            logging.debug("character {} is in one".format(i))
        else:
            logging.debug("Found the top middle segment character: {}".format(i))
            segdict['topmid'] = i
    return segdict

def getMidMid(numDict, segDict, signal):
    """
    Take all of the five count numbers commonality will give you the three middle
    numbers. and those with 4, and you'll get the 
    """
    midSeg = getMidSeg(signal)
    for c in midSeg:
        if c in numDict["four"]:
            logging.debug("Found the middle middle segment {}".format(c))
            segDict['midmid'] = c
            return segDict

def getTopLeft(numDict, segDict):
    """
    look at the 4 number, and then look at what's not the midmid segment, and
    in 1. that'll give me the topleft segment
    """
    for s in numDict['four']:
        if s not in numDict['one'] and s not in segDict['midmid']:
            segDict['topleft'] = s
            return segDict
        

def getZeroNumber(numDict, segDict, signal):
    """
    Look at all of the six count elements, what ever doesn't have the middle
    segment gives you the zero.
    """
    sixCount = getSixCount(signal)
    for s in sixCount:
        if segDict['midmid'] not in s:
            # Then that one is the zero
            numDict['zero'] = s
            return numDict

def getTwoNumber(numDict, signal):
    fiveCount = getFiveCount(signal)
    for f in fiveCount:
        if f not in numDict.values():
            numDict['two'] = f
            return numDict

def getThreeNumber(numDict, signal):
    """
    What ever combo has the three mids, and the 1 must be the 3
    """
    fiveCount = getFiveCount(signal)
    one = numDict['one']
    for f in fiveCount:
        if one[0] in f and one[1] in f:
            numDict['three'] = f
            return numDict
            
def getFiveNumber(numDict, segDict, signal):
    """
    Look at the topleft segment, and the five count numbers, which ever has topleft
    then that's the 5
    """
    fiveCount = getFiveCount(signal)
    for c in fiveCount:
        if segDict['topleft'] in c:
            numDict['five'] = c
            return numDict
  
def getSixNineNumber(numDict, signal):
    sixCount = getSixCount(signal)  
    for s in sixCount:
        if s not in numDict.values():
            if numDict['one'][0] in s and numDict['one'][1] in s:
                numDict['nine'] = s
            else:
                numDict['six'] = s
    return numDict

def get_key(val, dictionary):
    for key, value in dictionary.items():
        if sorted(val) == sorted(value):
            return key


def PartOne(inputs):
    dumbNumberCount = 0
    for i in inputs:
        output = i[-4:]
        logging.debug("output values are: {}".format(output))
        for j in output:
            if len(j) in [2,3,4,7]:
                dumbNumberCount += 1
    print("Dumb number count this is:", dumbNumberCount)
    return dumbNumberCount

def PartTwo(inputs):
    """
    User the input part to select the numbers. Should be able to follow a set
    logic to get the results. Want to get each line segment. Should be able to
    get each segment eventually.
    
    """
    numberDictionary = {}
    segmentDictionary = {}
    grandTotal = 0
    for i in inputs:
        signal = i[:-4]
        output = i[-4:]
        logging.debug("output values are: {}".format(output))
        # Get the four known numbers
        numberDictionary = getKnownNumbers(signal, numberDictionary)
        segmentDictionary = getTopMid(numberDictionary['one'], numberDictionary['seven'], segmentDictionary)
        segmentDictionary = getMidMid(numberDictionary, segmentDictionary, signal)
        numberDictionary = getZeroNumber(numberDictionary, segmentDictionary, signal)
        numberDictionary = getThreeNumber(numberDictionary, signal)
        segmentDictionary = getTopLeft(numberDictionary, segmentDictionary)
        numberDictionary = getFiveNumber(numberDictionary, segmentDictionary, signal)
        numberDictionary = getTwoNumber(numberDictionary, signal)
        numberDictionary = getSixNineNumber(numberDictionary, signal)
        logging.info(numberDictionary)
        logging.debug(segmentDictionary)
        
        # Now I have all of my inputs. Figure out what the output numbers are. 
        outputString = ''
        logging.debug(output)
        for n in output:
            number = get_key(n, numberDictionary)
            if number == 'one':
                outputString += '1'
            elif number == 'two':
                outputString += '2'
            elif number == 'three':
                outputString += '3'
            elif number == 'four':
                outputString += '4'
            elif number == 'five':
                outputString += '5'
            elif number == 'six':
                outputString += '6'
            elif number == 'seven':
                outputString += '7'
            elif number == 'eight':
                outputString += '8'
            elif number == 'nine':
                outputString += '9'
            elif number == 'zero':
                outputString += '0'
            else:
                logging.warning("Number not found")
                logging.warning(n)
                logging.warning(number)
        logging.debug(outputString)
        grandTotal += int(outputString)
    print("The grand total is", grandTotal)
            
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    
    args = parser.parse_args()
    
    logging.basicConfig(level=args.dl)
    
    with open(args.path, 'r') as file:
        inputs = []
        for line in file:
            inputs.append(re.findall("[a-z]+", line))
    logging.debug(inputs)
    
    PartOne(inputs)
    PartTwo(inputs)