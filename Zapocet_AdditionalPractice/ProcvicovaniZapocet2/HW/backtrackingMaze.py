import numpy as np

def solve_maze(maze:np.array, x:int, y:int)->bool:
    # 1. Check boundaries
    if x>= maze.shape[0] or y>= maze.shape[1] or x<0 or y<0:
        return False
    
    # 2. Check if we hit a wall or our own path
    if maze[x,y] == '1' or maze[x,y] == "X":
        return False

    # 3. Check if we found the exit
    if maze[x][y] == '2':
        return True

    # --- THE BACKTRACKING STEP ---
    # CHOOSE
    original = maze[x,y]
    maze[x,y] = "X"

    # EXPLORE
    # Try all 4 directions. If ANY of them return True, we stop!
    if solve_maze(maze,x+1,y):
        return True
    if solve_maze(maze,x-1,y):
        return True
    if solve_maze(maze,x,y+1):
        return True
    if solve_maze(maze,x,y-1):
        return True

    # UN-CHOOSE (Backtrack)
    # If we get here, it means all 4 directions failed.
    maze[x,y] = original
    return False

# Example Maze
# '0' = path, '1' = wall, '2' = exit
board = np.array([
    ['0', '1', '0', '0'],
    ['0', '0', '0', '1'],
    ['1', '1', '0', '0'],
    ['0', '0', '1', '2']
])

if solve_maze(board, 0, 0):
    print("Path Found:")
    print(board)
else:
    print("No path possible.")