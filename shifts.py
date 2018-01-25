"""
shift all cells to corresponding extreme, combining adjacent equals.
"""


def right(n: int, grid1: list) -> list:
    grid = grid1
    for r in range(n):
        for c in range(n-2, -1, -1):
            grid = align_right(n, c, r, grid)
        for c in range(n-1, 0, -1):
            if grid[r][c-1] == grid[r][c] != 0:
                grid[r][c] += grid[r][c-1]
                grid[r][c-1] = 0
        for c in range(n-2, -1, -1):
            grid = align_right(n, c, r, grid)
    return grid


def align_right(n: int, c: int, r: int, grid1: list) -> list:
    grid = grid1
    if c < n - 1:
        if grid[r][c + 1] == 0:
            grid[r][c + 1], grid[r][c] = grid[r][c], 0
            return align_right(n, c+1, r, grid)
    return grid


def left(n: int, grid1: list) -> list:
    grid = grid1
    for r in range(n):
        for c in range(1, n):
            grid = align_left(n, c, r, grid)
        for c in range(1, n):
            if grid[r][c-1] == grid[r][c] != 0:
                grid[r][c-1], grid[r][c] = grid[r][c]*2, 0
        for c in range(1, n):
            grid = align_left(n, c, r, grid)
    return grid


def align_left(n: int, c: int, r: int, grid1: list) -> list:
    grid = grid1
    if c >= 1:
        if grid[r][c-1] == 0:
            grid[r][c-1], grid[r][c] = grid[r][c], 0
            return align_left(n, c-1, r, grid)
    return grid
    
    
def up(n: int, grid1: list) -> list:
    grid = grid1
    for c in range(n):
        for r in range(1, n):
            grid = align_up(n, c, r, grid)
        for r in range(1, n):  # do not check adjacent on bottom row.
            if grid[r-1][c] == grid[r][c] != 0:
                grid[r-1][c], grid[r][c] = grid[r][c]*2, 0
        for r in range(1, n):
            grid = align_up(n, c, r, grid)
    return grid
    

def align_up(n: int, c: int, r: int, grid1: list) -> list:
    grid = grid1
    if r >= 1:
        if grid[r-1][c] == 0:
            grid[r-1][c], grid[r][c] = grid[r][c], 0
            return align_up(n, c, r-1, grid)
    return grid
    
    
def down(n: int, grid1: list) -> list:
    grid = grid1
    for c in range(n):
        for r in range(n-1, -1, -1):
            grid = align_down(n, c, r, grid)
        for r in range(n-1, 0, -1):  # do not check adjacent on top row.
            if grid[r-1][c] == grid[r][c] != 0:
                grid[r][c], grid[r-1][c] = grid[r][c]*2, 0
        for r in range(n-1, -1, -1):
            grid = align_down(n, c, r, grid)
    return grid


def align_down(n: int, c: int, r: int, grid1: list) -> list:
    grid = grid1
    if r < n - 1:
        if grid[r+1][c] == 0:
            grid[r+1][c], grid[r][c] = grid[r][c], 0
            return align_down(n, c, r+1, grid)
    return grid
