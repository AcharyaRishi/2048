"""
search algorithms determine if moves and combinations are possible 
with cells
"""


def adjacent_search(n: int, grid: list, i: int) -> bool:
    x, y = i % n, i // n
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    ls = []
    for d in directions:
        if 0 <= x + d[0] < n:
            if 0 <= y + d[1] < n:
                ls.append((x + d[0], y + d[1]))
    for (x1, y1) in ls:
        if grid[x][y] == grid[x1][y1]:
            return True
    return False


def valid_grid(n: int, grid: list) -> bool:
    """
    will return True if grid can still be played on.
    will return False if no subsequent moves are possible.
    """

    # if grid contains no 0
    for l in grid:
        if 0 in l:
            return True

    # search adjacent pairs
    for i in range(n ** 2):
        if adjacent_search(n, grid, i):
            return True
    # if none, return False. Nothing more can be done
    return False
