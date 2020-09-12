#!/usr/bin/python3

import os
import random
import time
import copy

CELLS_WIDTH = 80
CELLS_HEIGHT = 30

def main():
    next_cells = []
    create_initial_configuration(next_cells)

    while True:
        os.system('clear')

        current_cells = copy.deepcopy(next_cells)
        print_cells(current_cells)

        calculate_new_cell_states(current_cells, next_cells)
        time.sleep(.1)

#------------------------------------------------------------------------------

def create_initial_configuration(cells):
    """ Construct the first configuration of the cellular automaton.
        '#' denotes a living cell
        ' ' denotes a blank

    Args:
        cells(list): the cellular automaton grid

    """
    for x in range(CELLS_WIDTH):
        column = []
        for y in range(CELLS_HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#')  # add a living cell
            else:
                column.append(' ')  # add a dead cell
        cells.append(column)


def print_cells(cells):
    """ Display the current configuration of the cellular automaton.

    Args:
        cells(list): the cellular automaton grid

    """
    for y in range(CELLS_HEIGHT):
        for x in range(CELLS_WIDTH):
            print(cells[x][y], end='')
        print()


def calculate_new_cell_states(current_cells, next_cells):
    """ Calculate the next configuration of the cellular automaton.

    Args:
        current_cells(list): The current cellular automaton snapshot
        next_cells(list): The next cellular automaton snapshot
    """
    for x in range(CELLS_WIDTH):
        for y in range(CELLS_HEIGHT):
            # get neighboring coordinates:
            # '%' ensures coordinates are within bounds
            left_coord = (x - 1) % CELLS_WIDTH
            right_coord = (x + 1) % CELLS_WIDTH
            above_coord = (y - 1) % CELLS_HEIGHT
            below_coord = (y + 1) % CELLS_HEIGHT

            # count number of living neighbors:
            number_of_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                number_of_neighbors += 1  # top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                number_of_neighbors += 1  # top neighbor is alive
            if current_cells[right_coord][above_coord] == '#':
                number_of_neighbors += 1  # top-right neighbor is alive
            if current_cells[left_coord][y] == '#':
                number_of_neighbors += 1  # left neighbor is alive
            if current_cells[right_coord][y] == '#':
                number_of_neighbors += 1  # right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                number_of_neighbors += 1  # bottom-left neighbor is alive
            if current_cells[x][below_coord] == '#':
                number_of_neighbors += 1  # bottom neighbor is alive
            if current_cells[right_coord][below_coord] == '#':
                number_of_neighbors += 1  # bottom-right neighbor is alive

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
