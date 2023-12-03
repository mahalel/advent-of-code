import re
from functools import reduce
from operator import mul
from collections import defaultdict

def input_to_grid(input):
    grid = []
    with open(input, 'r') as f:
        for line in f.readlines():
            grid.append(line.strip())
    return grid

def get_symbols(input):
    with open(input, "r") as f:
        content = f.read()
        symbols = set(re.findall(r"[^\d\.\n]", content))
    return symbols
 
def get_neighbors(grid, x, y):
    neighbors = []
    gears = ""
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[0]), y+2)):
            if (i, j) != (x, y):
                neighbors.append(grid[i][j])
                if grid[i][j] == "*":
                    gears = f"{i}-{j}"
    return set(neighbors), gears

def get_ratio(gears):
    ratio = 0
    for gear in gears:
        if len(gears[gear]) > 1:
            ratio += reduce(mul, gears[gear])
    return ratio 

def main(grid, symbols):
    total = 0
    gears = defaultdict(set)
    for row in range(len(grid)):
        matches = re.finditer(r"\d+", grid[row])
        for match in matches:
            neigh = set()
            start_index = match.start()
            end_index = match.end() - 1
            number = int(grid[row][start_index:end_index+1])
            for index in [start_index, end_index]:
                neighbors, gear = get_neighbors(grid, row, index)
                neigh.update(neighbors)
                gears[gear].update([number])
            if neigh.intersection(symbols):
                total += number
    gears.pop("") 
    ratio = get_ratio(gears)
    return total, ratio

input = "./input"
symbols = get_symbols(input)
grid = input_to_grid(input)

print(main(grid, symbols))