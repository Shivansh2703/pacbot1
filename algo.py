# You can modify this file to implement your own algorithm

from constants import *
import random

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

previous_direction = 0
def find_neighbors(grid, location, search_range=1):
    valid_neighbors = []
    
    for i in range(-1 * search_range, search_range+1):
        for j in range(-1 * search_range, search_range+1):
            if not (i == 0 and j == 0):
                curr_loc = [location[0] + i, location[1] + j]
            
                if check_valid_location(grid, curr_loc) and grid[curr_loc[0]][curr_loc[1]] == 2:
                    valid_neighbors.append(curr_loc)
                    
    # random.shuffle(valid_neighbors)
    return valid_neighbors
                
def get_move_to_location(grid, prev_dir, current_location, destination_location):
    global previous_direction
    possible_moves = []
    
    for i in [-1, 1]:
        if check_valid_move(grid, [current_location[0]+i, current_location[1]]):
            possible_moves.append([i, 0])

        if check_valid_move(grid, [current_location[0], current_location[1]+i]):
            possible_moves.append([0, i])
    
    # move_distances = [get_distance(x, destination_location) for x in possible_moves]
    move_distances = []
    for x in possible_moves:
        if x == prev_dir:
            move_distances.append(get_distance([current_location[0]+x[0], current_location[1]+x[1]], destination_location) - random.randint(0, 3))
        else:
            move_distances.append(get_distance([current_location[0]+x[0], current_location[1]+x[1]], destination_location))
    
    chosen_move = possible_moves[move_distances.index(min(move_distances))]
    previous_direction = [chosen_move[0], chosen_move[1]]
    return [current_location[0] + chosen_move[0], current_location[1] + chosen_move[1]]

def check_valid_move(grid, next_location):
    if check_valid_location(grid, next_location) and grid[next_location[0]][next_location[1]] != 1:
        return True
    return False
    
def check_valid_location(grid, location):
    if location[0] >= 0 and location[0] < len(grid) and location[1] >= 0 and location[1] < len(grid[0]):
        return True
    
    return False

def get_distance(c_loc, d_loc):
    
    return ((c_loc[0] - d_loc[0]) ** 2 + (c_loc[1] - d_loc[1]) ** 2) ** 0.5

def get_next_coordinate(grid, location):

    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.

    Parameters:
    - grid (list of lists): A 2D array representing the game board.
    - location (list): The current location of the 6ix-pac in the form (x, y).

    Returns:
    - list or tuple: 
        - If the next coordinate is valid, return the next coordinate in the form (x, y) or [x,y].
        - If the next coordinate is invalid, return None.
    """
    global previous_direction
    search_range = 1
    
    while search_range < 35:

        neighbors = find_neighbors(grid, location, search_range)
        
        if len(neighbors):
            neighbors_distances = [get_distance(location, x) for x in neighbors]
            print("Next location", neighbors[neighbors_distances.index(min(neighbors_distances))])
            print("Next move", get_move_to_location(grid, previous_direction, location, neighbors[neighbors_distances.index(min(neighbors_distances))]))
            return get_move_to_location(grid, previous_direction, location, neighbors[neighbors_distances.index(min(neighbors_distances))])
        
        search_range += 1
            
            
    return None