"""A graphical display of a cave represented as a rectangular grid of characters"""
import graphics.grid
import graphics.grid as grid_view

import cave

# Size of displayed grid;
# n_rows == 0 is also interpreted as "there is no current display"
#
n_rows = 0
n_cols = 0

# Water color can be changed, e.g., as we
# move from chamber to chamber
current_water = graphics.grid.get_cur_color()


def display(cavern: list[list[str]], width: int, height: int):
    """Create a graphical representation of cave using the grid.
    This graphical representation can be further manipulated
    (e.g., filling cave cells with water of various colors)
    with fill_cell.
    """
    global n_rows, n_cols
    n_rows = len(cavern)
    n_cols = len(cavern[0])
    grid_view.make(n_rows, n_cols, width, height)
    for row in range(n_rows):
        for col in range(n_cols):
            if cavern[row][col] == cave.STONE:
                grid_view.fill_cell(row, col, grid_view.black)
            elif cavern[row][col] == cave.WATER:
                grid_view.fill_cell(row, col, current_water)
    return


def change_water():
    """Switch to a new color of water"""
    global current_water
    current_water = graphics.grid.get_next_color()


def fill_cell(row: int, col: int):
    """Fill display of cave[row][col] with current colored water"""
    # NOTE:  We need this to be a "do-nothing" function if there is no current display,
    # as will be the case when running doctests.  We take n_rows == 0 as
    # our signal that there is no display.
    if n_rows == 0:
        return
    assert 0 <= row < n_rows, f"Row must be in range 0..{n_rows - 1} "
    assert 0 <= col < n_cols, f"Column must be in range 0..{n_cols - 1}"
    grid_view.fill_cell(row, col, color=current_water)


def prompt_to_close():
    """Prompt the user before closing the display"""
    input("Press enter to close display")
    grid_view.win.close()
    n_rows = 0
    n_cols = 0











