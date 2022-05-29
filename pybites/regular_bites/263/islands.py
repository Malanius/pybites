from typing import List, Tuple


Grid = List[List[int]]
ISLAND = 1
VISITED_ISLAND = 4
SEA = 0


def count_islands(grid: Grid) -> int:
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0
    while has_islands(grid):
        x, y = find_island(grid)
        flood_fill_island(x, y, grid)
        islands += 1
    return islands


def has_islands(grid: Grid) -> bool:
    """
    Checks if the grid has any islands.
    Input: grid
    """
    for row in grid:
        for col in row:
            if col == ISLAND:
                return True
    return False


def find_island(grid: Grid) -> Tuple[int, int]:
    """
    Input: the grid
    Output: the first island's coordinates
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ISLAND:
                return row, col


def flood_fill_island(x: int, y: int, grid: Grid):
    """
    Flood fill the island starting from the given coordinates.
    Input: x, y coordinates of the island, grid map
    """
    # check if the coordinates are valid
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return

    # skip if the cell is already visited or not an island
    if grid[x][y] != ISLAND:
        return

    # mark the cell as visited
    grid[x][y] = VISITED_ISLAND

    # flood fill surrounding cells
    flood_fill_island(x + 1, y, grid)
    flood_fill_island(x - 1, y, grid)
    flood_fill_island(x, y + 1, grid)
    flood_fill_island(x, y - 1, grid)
