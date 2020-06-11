import os
import random, time, copy

WIDTH = 60
HEIGHT = 20

def main():
    next_cells = []
    create_cells(next_cells)

    while True:
        os.system('clear')

        current_cells = copy.deepcopy(next_cells)
        print_cells(current_cells)

        calculate_new_cell_states(current_cells, next_cells)
        time.sleep(.2)

#------------------------------------------------------------------------------

def create_cells(next_cells):
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0,1) == 0:
                column.append('#') # add a living cell
            else:
                column.append(' ') # add a dead cell
        next_cells.append(column) # next_cells is a list of column lists


def print_cells(current_cells):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # print the '#' or space
        print()


def calculate_new_cell_states(current_cells, next_cells):
         # calculate the next step's cells based on current step's cells
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # get neighboring coordinates:
                # % ensures coordinates are within bounds
                left_coordinate = (x - 1) % WIDTH
                right_coordinate = (x + 1) % WIDTH
                above_coordinate = (y - 1) % HEIGHT
                below_coordinate = (y + 1) % HEIGHT

                # count number of living neighbors:
                number_of_neighbors = 0
                if current_cells[left_coordinate][above_coordinate] == '#':
                    number_of_neighbors += 1 # top-left neighbor is alive
                if current_cells[x][above_coordinate] == '#':
                    number_of_neighbors += 1 # top neighbor is alive
                if current_cells[right_coordinate][above_coordinate] == '#':
                    number_of_neighbors += 1 # top-right neighbor is alive
                if current_cells[left_coordinate][y] == '#':
                    number_of_neighbors += 1 # left neighbor is alive
                if current_cells[right_coordinate][y] == '#':
                    number_of_neighbors += 1 # right neighbor is alive
                if current_cells[left_coordinate][below_coordinate] == '#':
                    number_of_neighbors += 1 # bottom-left neighbor is alive
                if current_cells[x][below_coordinate] == '#':
                    number_of_neighbors += 1 # bottom neighbor is alive
                if current_cells[right_coordinate][below_coordinate] == '#':
                    number_of_neighbors += 1 # bottom-right neighbor is alive

                # set cell based on Conway's Game of Life rules:
                if current_cells[x][y] == '#' and (number_of_neighbors == 2 or
                                               number_of_neighbors == 3):
                    # living cells with 2 or 3 neighbors stay alive:
                    next_cells[x][y] == '#'
                elif current_cells[x][y] == ' ' and number_of_neighbors == 3:
                    # dead cells with 3 neighbors become alive:
                    next_cells[x][y] = '#'
                else:
                    # everything else dies or stays dead:
                    next_cells[x][y] = ' '


main()
