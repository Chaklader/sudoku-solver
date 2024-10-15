from utils import *
from functools import reduce

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units

diag1 = [rows[i] + cols[i] for i in range(len(rows))]
diag2 = [rows[i] + cols[len(cols) - 1 - i] for i in range(len(rows))]
unitlist = unitlist + [diag1, diag2]

# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)

"""
Sudoku Solving Rules and Strategies:
    1. If a box has a value, then all the boxes in the same row, same column, or same 3x3 square cannot have that same value.
    2. If there is only one allowed value for a given box in a row, column, or 3x3 square, then the box is assigned that value.
    3. The individual squares at the intersection of rows and columns are called 'boxes'. These boxes have labels 'A1', 'A2', ..., 'I9'.
    4. The complete rows, columns, and 3x3 squares, are called 'units'. Each unit is a set of 9 boxes, and there are 27 units in total.
    5. For a particular box (such as 'A1'), its 'peers' are all other boxes that belong to a common unit (namely, those that belong to the same row, column, or 3x3 square).
"""


def naked_twins(values):
    """Eliminate values using the naked twins strategy."""

    def find_twins(box):
        """Find all twins for a given box."""
        return [peer for peer in peers[box]
                if values[box] == values[peer] and len(values[box]) == 2]

    def eliminate_from_peers(box, twin):
        """Eliminate digits of the twin from the peers of both boxes."""
        common_peers = set(peers[box]) & set(peers[twin])
        digits = values[box]
        return {peer: ''.join(d for d in values[peer] if d not in digits)
                for peer in common_peers}

    # Find all boxes with potential twins
    potential_twins = filter(lambda box: len(values[box]) == 2, values)

    # Find actual twins and their eliminations
    eliminations = [eliminate_from_peers(box, twin)
                    for box in potential_twins
                    for twin in find_twins(box)]

    # Merge all eliminations
    merged_eliminations = {}
    for elimination in eliminations:
        merged_eliminations.update(elimination)

    # Apply eliminations to a copy of the input values
    return {**values, **merged_eliminations}


def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies"""

    strategies = [eliminate, only_choice, naked_twins]

    def apply_strategy(vals, strategy):
        return strategy(vals)

    def count_solved_values(vals):
        return sum(1 for box in vals if len(vals[box]) == 1)

    while True:
        solved_before = count_solved_values(values)
        values = reduce(apply_strategy, strategies, values)

        if not values or count_solved_values(values) == solved_before:
            break

    return values if all(len(val) > 0 for val in values.values()) else False


def search(values):
    """Apply depth first search to solve Sudoku puzzles"""

    def find_min_possibilities(vals):
        unsolved = ((len(vals[s]), s) for s in boxes if len(vals[s]) > 1)
        return min(unsolved, key=lambda x: x[0])

    values = reduce_puzzle(values)
    if not values:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values

    _, s = find_min_possibilities(values)

    return next(filter(None, (search(assign_value(values.copy(), s, value))
                              for value in values[s])), False)


def assign_value(values, box, value):
    """Assign a value to a box and propagate constraints"""
    values[box] = value
    return reduce_puzzle(values)


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku

        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
