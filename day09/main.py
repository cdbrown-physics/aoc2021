import logging
import argparse
import sys
import re
sys.path.append('..')
import constants

def makeMap(path):
    with open(args.path, 'r') as file:
        # Make the line fromt he file and make it a list of ints
        positions = {}
        row = 0
        for line in file:
            lineInt = [int(x) for x in re.findall("[0-9]", line)]
            col = 0
            for i in lineInt:
                key = "{},{}".format(row, col)
                positions[key] = i
                col += 1
            row += 1
            
    return positions, row, col

def PartOne(args):
    positions, rowmax, colmax = makeMap(args.path)
    positions[None] = constants.LARGE_NUMBER
    risk_total = 0
    low_points = []
    for c in range(colmax):
        for r in range(rowmax):
            key = "{},{}".format(r, c)
            if positions[key] == 9:
                continue
            else:
                keyup = "{},{}".format(r+1, c)
                keydown = "{},{}".format(r-1, c)
                keyleft = "{},{}".format(r, c-1)
                keyright = "{},{}".format(r, c+1)
                
                if keyup not in positions:
                    keyup = None
                if keydown not in positions:
                    keydown = None
                if keyleft not in positions:
                    keyleft = None
                if keyright not in positions:
                    keyright = None

                if positions[keyup] > positions[key] and positions[keydown] > positions[key] and positions[keyleft] > positions[key] and positions[keyright] > positions[key]:
                    risk_level = positions[key] + 1
                    low_points.append(key)
                    risk_total += risk_level
    print("Total risk level is", risk_total)
    return positions, low_points

def PartTwo(positions, lowPoints):
    for lowpoint in lowPoints:
        area = 1
        

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", type=int, default=30)
    parser.add_argument("--path", type=str, default="testinput.txt")
    args = parser.parse_args()
    print(args)
    
    positions, lowPoints = PartOne(args)
    PartTwo(positions, lowPoints)
    
    
            
        
    