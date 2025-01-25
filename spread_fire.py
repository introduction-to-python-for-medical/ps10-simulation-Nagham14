
    # Set the center tree on fire
    grid[grid_size // 2][grid_size // 2] = 2

    return grid

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)  # Determine the grid size
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # Tree that isn't burning yet
                neighbors = []
                # Check all 4 neighbors, ensuring we stay within bounds
                if i > 0: 
                    neighbors.append(grid[i - 1][j])  # Top neighbor
                if i < grid_size - 1: 
                    neighbors.append(grid[i + 1][j])  # Bottom neighbor
                if j > 0: 
                    neighbors.append(grid[i][j - 1])  # Left neighbor
                if j < grid_size - 1: 
                    neighbors.append(grid[i][j + 1])  # Right neighbor
                
                if 2 in neighbors:  # Fire spreads to this tree
                    update_grid[i][j] = 2

    return update_grid
