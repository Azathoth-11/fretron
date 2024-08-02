'''
The appoach to this question is to use backtracking to find all possible paths from the starting point to the special castle.
Given the base condition as reaching the special castle, 
we have to options when we encounter a soldier 1. kill, 2. jump over if there a solider to kill forward.
we keep on doing this division till we find all the paths.
I have drawned a graph to better illustrate the approach.
'''
BOARD_SIZE = 9

soldier_positions = [(0, 0), (7, 8), (0, 8), (3, 0), (3, 1), (3, 7), (1, 5), (4, 5), (7, 1), (4, 8), (1, 7)]
castle_start = (0, 1)
special_castle = (1, 2)

def initialize_board():
    board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for x, y in soldier_positions:
        board[x][y] = 'S'
    return board

def in_bounds(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def move_forward(x, y, direction):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return (x + directions[direction][0], y + directions[direction][1])

def jump(x, y, direction):
    next_pos = move_forward(x, y, direction)
    if in_bounds(next_pos[0], next_pos[1]) and next_pos in soldiers:
        jump_pos = move_forward(next_pos[0], next_pos[1], direction)
        if in_bounds(jump_pos[0], jump_pos[1]) and jump_pos not in soldiers:
            return jump_pos
    return None

# Backtracking
def find_paths(board, x, y, dir_idx, path, paths, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    if (x, y) == special_castle and len(path) > 1:
        paths.append(list(path))
        return

    if (x, y, dir_idx) in visited:
        return
    visited.add((x, y, dir_idx))
    
    while in_bounds(x + directions[dir_idx][0], y + directions[dir_idx][1]):
        x, y = move_forward(x, y, dir_idx)
        if board[x][y] == 'S':
            # Kill and go left
            path.append((x, y))
            board[x][y] = '.'
            find_paths(board, x, y, (dir_idx + 1) % 4, path, paths, visited)
            board[x][y] = 'S'
            path.pop()
            
            # Jump over
            jump_pos = jump(x, y, dir_idx)
            if jump_pos and jump_pos not in soldiers:
                path.append((x, y))
                find_paths(board, jump_pos[0], jump_pos[1], dir_idx, path, paths, visited)
                path.pop()
        elif board[x][y] == '.' and len(path) > 1:
            path.append((x, y))
            find_paths(board, x, y, dir_idx, path, paths, visited)
            path.pop()

def print_paths(paths):
    for idx, path in enumerate(paths):
        print(f"Path {idx + 1}")
        print("=" * 7)
        print(f"Start: {path[0]}")
        for i in range(1, len(path)):
            current = path[i - 1]
            next_pos = path[i]
            if next_pos in soldier_positions:
                print(f"{current} -> Kill at {next_pos}. Then, turn Left.")
            else:
                if path[i - 1] != next_pos:
                    print(f"{current} -> Jump over {next_pos}")
        print(f"Arrive at {path[-1]}\n")

def main():
    board = initialize_board()
    global soldiers
    soldiers = set(soldier_positions)
    paths = []
    visited = set()
    find_paths(board, castle_start[0], castle_start[1], 0, [castle_start], paths, visited)
    
    # Remove duplicates
    unique_paths = []
    unique_path_set = set()
    for path in paths:
        path_tuple = tuple(path)
        if path_tuple not in unique_path_set:
            unique_path_set.add(path_tuple)
            unique_paths.append(path)

    print_paths(unique_paths)

if __name__ == "__main__":
    main()
