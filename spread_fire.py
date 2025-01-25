import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):  # Iterate over all rows
        for j in range(grid_size):  # Iterate over all columns
            if grid[i][j] == 1:  # If the cell contains a tree
                neighbors = []
                
                if i > 0:  # Check above
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # Check below
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Check left
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # Check right
                    neighbors.append(grid[i][j+1])

                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
