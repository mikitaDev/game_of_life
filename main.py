from pprint import pprint
from random import choice
from typing import List

#const 
GENERATIONS = 10
SIZE = 5

def create_map(size: int = SIZE) -> List[List[bool]]:
    return [[choice([True,False]) for _ in range (SIZE)] for _ in range(SIZE)]

def show_map ( map_ : List[List[bool]]) :
    print("##################")
    pprint(map_)
    
def get_neighbours(map_, coordinate_row, coordinate_column) -> int:
    count = 0
    # 1 2 3
    # 4 * 6
    # 7 8 9
    for row in range(coordinate_row - 1, coordinate_row + 2):
            for column in range(coordinate_column - 1, coordinate_column + 2):
                if row < 0 or column < 0:
                    continue
                if row == coordinate_row and column == coordinate_column:
                    continue
                if row >= SIZE or column >= SIZE:
                    continue
                count+=map_[row][column]
    return count

def update_map(old_map : List[List[bool]]) -> List[List[bool]]:
    
    new_map = old_map.copy()
                   
    for row in range(SIZE):
        for column in range(SIZE):
            count = get_neighbours(old_map,row,column)
            if count == 2 or count == 3 and old_map[row][column]:
                new_map[row][column] = True
            elif not old_map[row][column] and count == 3:
                new_map[row][column] = False
            else :
                new_map[row][column] = False
    return new_map
            

if __name__ == '__main__':
    current_map = create_map()
    
    # start
    print("start filed")
    show_map(current_map)
    
    for count in range(GENERATIONS):
        print("iteration = ", count)
        current_map = update_map(current_map)
        show_map(current_map)

