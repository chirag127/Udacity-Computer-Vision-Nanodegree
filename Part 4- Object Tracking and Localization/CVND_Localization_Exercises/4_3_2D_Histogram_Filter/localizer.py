# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for _ in range(height):
        row = [belief_per_cell for _ in range(width)]
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    #
    # TODO - implement this in part 2
    #

    return []

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for _ in range(width)] for _ in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)