def dfs_recursive(grid, row, col, visited,wall_h,wall_v, From = None):
    rows, cols = len(grid), len(grid[0])

    if row < 0 or \
        row >= rows or \
        col < 0 or \
        col >= cols or \
        visited[row][col]:
        return
    
    if (grid[row][col] != "0" and From != None):
        if From == "U":
            if wall_h[row-1][col] == "0":
                dfs_recursive(grid, row - 1, col, visited,wall_h,wall_v,"U")
                return
            else:
                dfs_recursive(grid, row - 1, col + 1,visited,wall_h,wall_v,None)
                dfs_recursive(grid, row - 1, col - 1,visited,wall_h,wall_v,None)
                return
        elif From == "D":
            if wall_h[row][col] == "0":
                dfs_recursive(grid, row + 1, col, visited,wall_h,wall_v,"D")
                return
            else:
                dfs_recursive(grid, row + 1, col + 1,visited,wall_h,wall_v,None)
                dfs_recursive(grid, row + 1, col - 1,visited,wall_h,wall_v,None)
                return
        elif From == "L":
            if wall_v[row][col] == "0":
                dfs_recursive(grid, row, col - 1, visited,wall_h,wall_v,"L")
                return
            else:
                dfs_recursive(grid, row + 1, col - 1,visited,wall_h,wall_v,None)
                dfs_recursive(grid, row - 1, col - 1,visited,wall_h,wall_v,None)
                return
        elif From == "R":
            if wall_v[row][col-1] == "0":
                dfs_recursive(grid, row, col + 1, visited,wall_h,wall_v,"R")
                return
            else:
                dfs_recursive(grid, row + 1, col + 1,visited,wall_h,wall_v,None)
                dfs_recursive(grid, row - 1, col + 1,visited,wall_h,wall_v,None)
                return
        
    if (From == "D" and wall_h[row-1][col] == "1") or \
        (From == "U" and wall_h[row][col] == "1") or \
        (From == "R" and wall_v[row][col-1] == "1")   or \
        (From == "L" and wall_v[row][col] == "1"):
        return
    
    # Mark the current cell as visited
    visited[row][col] = True
    #print(f"Visiting cell ({row}, {col}) with value {grid[row][col]}")
    
    # Visit all neighboring cells (up, down, left, right)
    dfs_recursive(grid, row - 1, col, visited,wall_h,wall_v,"U")  # Up
    dfs_recursive(grid, row + 1, col, visited,wall_h,wall_v, "D")  # Down
    dfs_recursive(grid, row, col - 1, visited,wall_h,wall_v, "L")  # Left
    dfs_recursive(grid, row, col + 1, visited,wall_h,wall_v, "R")  # Right
