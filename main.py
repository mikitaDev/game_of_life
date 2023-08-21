from pprint import pprint
from random import choice
from typing import List

#const 
GENERATIONS = 10
SIZE = 5

def create_map(size: int = SIZE) -> List[List[bool]]:
    return [[choice([1,0]) for _ in range (SIZE)] for _ in range(SIZE)]

def show_map ( map_ : List[List[bool]]) :
    print("##################")
    pprint(map_)
    
def get_neighbours(map_, coordinate_row, coordinate_column) -> int:
    count = 0
    # 1 2 3
    # 4 * 6
    # 7 8 9
    if( coordinate_row != 0 and coordinate_column != 0 and map_[coordinate_row - 1][coordinate_column - 1] == 1):
        count += 1
        
    if(coordinate_row != 0 and coordinate_column != SIZE -1 and map_[coordinate_row - 1][coordinate_column + 1] == 1):
        count += 1
            
    if( coordinate_row != 0 and map_[coordinate_row - 1][coordinate_column] == 1 ):
        count += 1
    ############################
    if(coordinate_column != SIZE -1 and map_[coordinate_row][coordinate_column + 1] == 1 ):
        count += 1
           
    if(coordinate_column != 0 and  map_[coordinate_row][coordinate_column - 1] == 1):
        count += 1

    #############################
    if(coordinate_row != SIZE -1 and coordinate_column != SIZE -1 and map_[coordinate_row + 1][coordinate_column + 1] == 1):
        count += 1

    if(coordinate_row != SIZE -1  and coordinate_column != 0 and  map_[coordinate_row + 1][coordinate_column - 1] == 1):
        count += 1
        
    if(coordinate_row != SIZE -1 and  map_[coordinate_row + 1][coordinate_column] == 1):
        count += 1
        
    return count

def update_map(old_map : List[List[bool]]) -> List[List[bool]]:
    
    new_map = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
               
    for row in range(SIZE):
        for column in range(SIZE):
            count = get_neighbours(old_map,row,column)
            if(count == 2 or count == 3):
                new_map[row][column] = 1
            else:
                new_map[row][column] = 0
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

