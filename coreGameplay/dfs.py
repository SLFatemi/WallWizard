def dfs_recursive(grid, row, col, visited, wall_h, wall_v, From=None):
    rows, cols = len(grid), len(grid[0])

    if (grid[row][col] != "0" and From != None):
        if From == "U":
            if wall_h[row - 1][col] == False:
                dfs_recursive(grid, row - 1, col, visited, "U")
                return
            else:
                dfs_recursive(grid, row - 1, col + 1, visited, None)
                dfs_recursive(grid, row - 1, col - 1, visited, None)
                return
        elif From == "D":
            if wall_h[row][col] == False:
                dfs_recursive(grid, row + 1, col, visited, "D")
                return
            else:
                dfs_recursive(grid, row + 1, col + 1, visited, None)
                dfs_recursive(grid, row + 1, col - 1, visited, None)
                return
        elif From == "L":
            if wall_v[row][col] == False:
                dfs_recursive(grid, row, col - 1, visited, "L")
                return
            else:
                dfs_recursive(grid, row + 1, col - 1, visited, None)
                dfs_recursive(grid, row - 1, col - 1, visited, None)
                return
        elif From == "R":
            if wall_v[row][col - 1] == False:
                dfs_recursive(grid, row, col + 1, visited, "R")
                return
            else:
                dfs_recursive(grid, row + 1, col + 1, visited, None)
                dfs_recursive(grid, row - 1, col + 1, visited, None)
                return

    if row < 0 or \
            row >= rows or \
            col < 0 or \
            col >= cols or \
            visited[row][col] or \
            (From == "D" and wall_h[row - 1][col]) or \
            (From == "U" and wall_h[row][col]) or \
            (From == "R" and wall_v[row][col - 1]) or \
            (From == "L" and wall_v[row][col]):
        return

    # Mark the current cell as visited
    visited[row][col] = True
    # print(f"Visiting cell ({row}, {col}) with value {grid[row][col]}")

    # Visit all neighboring cells (up, down, left, right)
    dfs_recursive(grid, row - 1, col, visited, "U")  # Up
    dfs_recursive(grid, row + 1, col, visited, "D")  # Down
    dfs_recursive(grid, row, col - 1, visited, "L")  # Left
    dfs_recursive(grid, row, col + 1, visited, "R")  # Right
