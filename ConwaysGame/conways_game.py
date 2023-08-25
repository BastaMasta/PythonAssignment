import copy
import random
import sys
import time
from os import system, name

# Set up the constants:
WIDTH = 50  # The width of the cell grid.
HEIGHT = 30  # The height of the cell grid.

ALIVE = '🟨'  # The character representing a living cell.
DEAD = '🟪'  # The character representing a dead cell.

nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # Loop over every possible column.
    for y in range(HEIGHT):  # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE  # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD  # Add a dead cell.

while True:

    # Clear Terminal/Console Screen for every iteration
    if name == 'nt':
        _ = system('cls')  # For windows
    else:
        _ = system('clear')  # For Linux ond OSX

    print("="*38, "Conway's Game of Life", "="*38)
    print("\t\t\t\t\t\t\t\t   By Sameed Ahmed, USN: 2VX22CB043")

    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the cell status
        print()  # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # Top-left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # Add a 1-second pause to reduce flickering, and to slow down the game.
    except KeyboardInterrupt:
        print("\nThank you for playing my render of Conway's Game of Life!")
        print("\nMade By: Sameed Ahmed, USN: 2VX22CB043\n\n")
        sys.exit()  # When Ctrl-C is pressed, end the program.
