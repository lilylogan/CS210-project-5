"""Flood-fill to count chambers in a cave.
CS 210 project.
Lily Logan, October 24
Credits: TBD
"""

import doctest
import cave
import config
import cave_view

def scan_cave(cavern: list[list[str]]) -> int:
    """Scan the cave for air pockets. Return the number of
    air pockets encoutered.

    >>> cavern_1 = cave.read_cave("data/tiny-cave.txt")
    >>> scan_cave(cavern_1)
    1
    >>> cavern_2 = cave.read_cave("data/cave.txt")
    >>> scan_cave(cavern_2)
    3
    >>> cavern_3 = cave.read_cave("data/twisty-cave.txt")
    >>> scan_cave(cavern_3)
    7
    """
    air_pockets = 0
    for row_i in range(len(cavern)):
        for col_i in range(len(cavern[0])):
            if cavern[row_i][col_i] == cave.AIR:
                air_pockets += 1
                fill(cavern, row_i, col_i)
                cave_view.change_water()
    return air_pockets
            
def fill(cavern: list[list[str]], row_i: int, col_i: int):
    """Fill the whole chamber around cavern[row_i][col_i] with water
    """

    if (row_i >= 0 and row_i < len(cavern)
        and col_i >= 0 and col_i < len(cavern[0])
        and cavern[row_i][col_i] == cave.AIR):
        cavern[row_i][col_i] = cave.WATER
        cave_view.fill_cell(row_i, col_i)
        
        row_up_i = row_i - 1
        fill(cavern, row_up_i, col_i)
        
        row_down_i = row_i + 1
        fill(cavern, row_down_i, col_i)
        
        col_left_i = col_i - 1
        fill(cavern, row_i, col_left_i)
        
        col_right_i = col_i + 1
        fill(cavern, row_i, col_right_i)
    else:
        return 

def main():
    doctest.testmod()
    cavern = cave.read_cave(config.CAVE_PATH)
    cave_view.display(cavern, config.WIN_WIDTH, config.WIN_HEIGHT)
    scan_cave(cavern)
    cave_view.prompt_to_close()

if __name__ == "__main__":
    main()
