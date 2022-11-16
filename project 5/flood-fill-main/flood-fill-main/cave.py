"""Cave data structure for flood fill project
2022-09-22  Michal Young for CS 210 at U Oregon
CC-by-SA open source license

This module creates and returns a grid represented as a list-of-lists.
It can also manage an associated cavern display.
"""
import doctest

# Text symbols (single characters) for contents of grid
AIR = " "
STONE = "#"
WATER = "~"



def read_cave(cavern_path: str) -> list[list[str]]:
    """Build and return a cavern (grid of character cells)
    from specification found at cavern_path, which should be
    the path to a text file.   
    
    >>> read_cave("data/tiny_cave.txt")
    [['#', '#', '#', '#'], ['#', ' ', ' ', '#'], ['#', ' ', ' ', '#'], ['#', '#', '#', '#']]
    """
    cave = []
    cave_open = False
    with open(cavern_path, 'r') as cavern_file:
        for line in cavern_file:
            fields = line.split()
            command = fields[0]
            if command == "cave":
                assert len(fields) == 3, f"Syntax should be 'cave rows cols', got {line}"
                nrows = int(fields[1])
                ncols = int(fields[2])
                assert nrows > 0, "Rows should be a positive integer: {line}"
                assert ncols > 0, "Columns should be a positive integer: {line}"
                cave = new_cave(nrows, ncols)
                cave_open = True
            elif command == "hwall":
                assert cave_open, "First line should be 'cave rows cols'"
                assert len(fields) == 4, "Syntax 'hwall startrow startcol length'"
                assert cave_open, "cave command must precede hwall command"
                start_row = int(fields[1])
                start_col = int(fields[2])
                length = int(fields[3])
                assert start_row >= 0, "Start row must be integer, zero or greater"
                assert start_col >= 0, "Start column must be integer, zero or greater"
                assert length >= 1, "Length of wall must be integer, at least 1"
                assert start_col + length <= ncols, "Wall cannot extend beyond right edge"
                hwall(cave, start_row, start_col, length)
            elif command == "vwall":
                assert cave_open, "First line should be 'cave rows cols'"
                assert len(fields) == 4, "Syntax 'vwall startrow startcol length'"
                assert cave_open, "cave command must precede vwall command"
                start_row = int(fields[1])
                start_col = int(fields[2])
                length = int(fields[3])
                assert start_row >= 0, "Start row must be integer, zero or greater"
                assert start_col >= 0, "Start column must be integer, zero or greater"
                assert length >= 1, "Length of wall must be integer, at least 1"
                assert start_row + length <= nrows, "Wall cannot extend through floor"
                vwall(cave, start_row, start_col, length)
            else:
                print(f"**Command not understood: '{line}'")
    return cave


def new_cave(nrows: int, ncols: int):
    """Create and return a new cave with
    nrows rows and ncols columns, initially filled
    entirely with air.

    >>> new_cave(3, 4)
    [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    """
    cave = []
    for row in range(nrows):
        newRow = []
        cave.append(newRow)
        for col in range(ncols):
            newRow.append(AIR)
    return cave


def hwall(cave: list[list[str]], row: int, col: int, length: int):
    """Build a horizontal wall of stone starting from (row,col) and
    extending length cells to the right.

    >>> cave = new_cave(3, 3)
    >>> hwall(cave, 1, 1, 2)
    >>> cave
    [[' ', ' ', ' '], [' ', '#', '#'], [' ', ' ', ' ']]
    """
    for i in range(length):
        cave[row][col + i] = STONE


def vwall(cave: list[list[str]], row: int, col: int, length: int):
    """Build a vertical wall of stone starting from (row,col) and
    extending length cells down.

    >>> cave = new_cave(3, 3)
    >>> vwall(cave, 1, 1, 2)
    >>> cave
    [[' ', ' ', ' '], [' ', '#', ' '], [' ', '#', ' ']]
    """
    for i in range(length):
        cave[row + i][col] = STONE

def text(cave: list[list[str]]) -> str:
    """A textual version of the cave, for debugging

    >>> print(text([[' ', '#'], ['#', ' ']]))
    ----
    | #|
    |# |
    ----
    """
    if len(cave) == 0:
        return "(apparent cave-in; no cave)"
    top_bot_border = '-' * (len(cave[0]) + 2)
    txt_rows = [ top_bot_border ]
    for row in cave:
        txt_rows.append("|" + "".join(row) + "|")
    txt_rows.append(top_bot_border)
    return "\n".join(txt_rows)

