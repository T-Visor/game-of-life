#!/usr/bin/env python3

#############################################################################
# Description: The Game of Life, also known simply as Life,
#              is a cellular automaton devised by the British mathematician
#              John Horton Conway in 1970. It is a zero-player game,
#              meaning that its evolution is determined by its initial state,
#              requiring no further input. One interacts with the Game of
#              Life by creating an initial configuration and observing
#              how it evolves. It is Turing complete and can simulate
#              a universal constructor or any other Turing machine.
#
# Description Source: https://en.wikipedia.org/wiki/Conway's_Game_of_Life
#
# Author: T-Visor
##############################################################################

import os
import random
import time
import copy

DEAD_CELL = ' '
LIVING_CELL = '$'
CELLS_WIDTH = 80
CELLS_HEIGHT = 30

def main():
    """ 
        Observe Conway's Game of Life.
    """
    next_cells = []
    create_initial_configuration(next_cells)

    while True:
        os.system('clear')

        current_cells = copy.deepcopy(next_cells)
        print_cells(current_cells)

        calculate_new_cell_states(current_cells, next_cells)
        time.sleep(.1)


def create_initial_configuration(cells):
    """ 
        Construct the initial state of the cellular automaton.

    Args:
        cells (list): the matrix to be populated

    """
    for x in range(CELLS_WIDTH):
        column = []
        for y in range(CELLS_HEIGHT):
            if random.randint(0, 1) == 0:
                column.append(LIVING_CELL)
            else:
                column.append(DEAD_CELL)
        cells.append(column)


def print_cells(cells):
    """ 
        Display the current state of the cellular automaton.

    Args:
        cells (list): the cellular automaton matrix

    """
    for y in range(CELLS_HEIGHT):
        for x in range(CELLS_WIDTH):
            print(cells[x][y], end='')
        print()


def calculate_new_cell_states(current_cells, next_cells):
    """ 
        Calculate the next configuration of the cellular automaton.

    Args:
        current_cells (list): The current state of the cellular automaton

        next_cells (list): The next state of the cellular automaton based
                           on current_cells
    """
    for x in range(CELLS_WIDTH):
        for y in range(CELLS_HEIGHT):

            number_of_neighbors = get_living_neighbors(current_cells, x, y)

            # set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == LIVING_CELL and (number_of_neighbors == 2
                                                  or number_of_neighbors == 3):
                # living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] == LIVING_CELL
            elif current_cells[x][y] == DEAD_CELL and number_of_neighbors == 3:
                # dead cells with 3 neighbors become alive:
                next_cells[x][y] = LIVING_CELL
            else:
                # everything else dies or stays dead:
                next_cells[x][y] = DEAD_CELL


def get_living_neighbors(cells, x, y):
    """ 
        Count the number of living neighbors around a specified cell.

    Args:
        cells (list): The cellular automaton matrix

        x (int): x-coordinate of cell

        y (int): y-coordinate of cell

    Returns:
        the number of neighbors around the specified cell
    """
    # '%' ensures coordinates are within bounds
    left_coord = (x - 1) % CELLS_WIDTH
    right_coord = (x + 1) % CELLS_WIDTH
    above_coord = (y - 1) % CELLS_HEIGHT
    below_coord = (y + 1) % CELLS_HEIGHT

    number_of_neighbors = 0

    if cells[left_coord][above_coord] == LIVING_CELL:
        number_of_neighbors += 1  # top-left neighbor is alive
    if cells[x][above_coord] == LIVING_CELL:
        number_of_neighbors += 1  # top neighbor is alive
    if cells[right_coord][above_coord] == LIVING_CELL:
        number_of_neighbors += 1  # top-right neighbor is alive
    if cells[left_coord][y] == LIVING_CELL:
        number_of_neighbors += 1  # left neighbor is alive
    if cells[right_coord][y] == LIVING_CELL:
        number_of_neighbors += 1  # right neighbor is alive
    if cells[left_coord][below_coord] == LIVING_CELL:
        number_of_neighbors += 1  # bottom-left neighbor is alive
    if cells[x][below_coord] == LIVING_CELL:
        number_of_neighbors += 1  # bottom neighbor is alive
    if cells[right_coord][below_coord] == LIVING_CELL:
        number_of_neighbors += 1  # bottom-right neighbor is alive

    return number_of_neighbors


main()
