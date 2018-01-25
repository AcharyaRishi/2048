import shifts
import prompts
import searches


def main(n: int, grid1: list):
    """
    Main part of program repeats.
    Prompt --> input --> check if continue

    If can continue ==> call function again, prompt again
    If cannot continue ==> exit functions
    """
    
    grid = grid1  # duplicate to modify
    
    if not searches.valid_grid(n, grid):
        exit()
    
    grid = prompts.generate_prompt(n, grid)
    
    # ui1.print_grid(grid)

    def print_grid(grid2: list):
        places = 4
        for r in grid2:
            for c in range(n):
                if r[c] == 0:
                    print(" "*(places - 1)+"_", end="")
                else:
                    print(
                            " "*(places - len(str(r[c])))+str(r[c]),
                            end=""
                            )
            print()

    print_grid(grid)

    def get_input(n1: int, grid2: list):
        n, grid = n1, grid2
        command = input(
                "Type 'r' (right), 'l' (left),"
                "'u' (up), or 'd' (down)! \n"
                )
        if command == "u":
            grid = shifts.up(n, grid)
            main(n, grid)
        elif command == "d":
            grid = shifts.down(n, grid)
            main(n, grid)
        elif command == "r":
            grid = shifts.right(n, grid)
            main(n, grid)
        elif command == "l":
            grid = shifts.left(n, grid)
            main(n, grid)
        else:
            get_input(n, grid)

    get_input(n, grid)

def play(n: int):
    grid = [[0 for i in range(n)] for j in range(n)]
    main(n, grid)

# Console start.


play(6)
