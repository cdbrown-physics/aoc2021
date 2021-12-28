import logging
import argparse
import sys

def PartOne(args):
    position = [0, 0]
    
    with open(args.path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(' ')
            direction = line[0]
            distance = int(line[1])
            
            if direction.lower() == "forward":
                position[0] += distance
            elif direction.lower() == "down":
                position[1] += distance
            elif direction.lower() == "up":
                position[1] -= distance
            else:
                sys.exit("invalid direction")
    print("Answer to part one is", position[0] * position[1])
    
def PartTwo(args):
    aim = 0
    horizontal = 0
    depth = 0
    
    with open(args.path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(' ')
            direction = line[0]
            distance = int(line[1])
            
            if direction.lower() == "forward":
                horizontal += distance
                depth += aim * distance
            elif direction.lower() == "down":
                aim += distance
            elif direction.lower() == "up":
                aim -= distance
            else:
                sys.exit("invalid direction")
                
    print("Answer to part two is", depth * horizontal)    

 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dl", help="Debug level", default=20, type=int)
    parser.add_argument("--path", help="Path to the input file we want to use", type=str)
    args = parser.parse_args()
    
    PartOne(args)
    PartTwo(args)