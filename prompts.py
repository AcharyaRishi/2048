import random  # uses: location for prompt, value of prompt


def give_val() -> int:
    # give biased random integer. 5/6 chance of 2, 1/6 chance of 4
    if random.randint(1, 300) >= 280:
        a = 4
    else:
        a = 2
    return a


def generate_prompt(n: int, grid1: list) -> list:
    # find empty space, implant random prompt
    for r in grid1:
            if 0 in r:
                break
    else:
        return grid1

    grid = grid1
    x = random.randint(0, n - 1)  # locate random point
    y = random.randint(0, n - 1)
    if grid[x][y] == 0:
        grid[x][y] = give_val()  # implant if empty
    else:
        grid = generate_prompt(n, grid)  # try again if full
    return grid
