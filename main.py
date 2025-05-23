DUNGEON_MAP = [[-2, -3, 3],
               [-5, -30, 1],
               [10, -2, -8],
               [-10, 7, -5]]

GOLD_MAP = [[1, 0, 2],
            [0, 100, 1],
            [2, 3, 5],
            [20, 1, 2]]

STARTING_HP = 50

def combine_maps(map_a, map_b):
    """Combine two 2D maps into a single map."""
    return [list(zip(row_a, row_b)) for row_a, row_b in zip(map_a, map_b)]

def find_all_paths(grid):
    """
    Find all possible paths from top-left to bottom-right in a 2D grid.
    You can only move down or right.

    Args:
        grid: 2D list of integers

    Returns:
        List of paths, where each path is a list of (row, col) coordinates
    """

    rows = len(grid)
    cols = len(grid[0])
    all_paths = []

    def dfs(row, col, current_path):
        """Depth-first search to find all paths.
        Args:
            row: Current row index
            col: Current column index
            current_path: List of coordinates in the current path

        Returns:
            List of coordinates describing all valid paths

        """
        # Add current position to path
        current_path.append((row, col))

        # If we reached bottom-right corner, save this path into all_paths
        if row == rows - 1 and col == cols - 1:
            all_paths.append(current_path.copy())
        else:
            # Try moving right
            if col + 1 < cols:
                dfs(row, col + 1, current_path)

            # Try moving down
            if row + 1 < rows:
                dfs(row + 1, col, current_path)

        # Backtrack to last still valid cell
        current_path.pop()

    # Start dfs from top left corner (0, 0)
    dfs(0, 0, [])
    return all_paths


def find_best_solution(grid, paths):
    """
    Print all paths with their corresponding values from the grid.

    Args:
        grid: 2D list of integers
        paths: List of coordinate paths
    """

    results_so_far = []
    for path_idx, path in enumerate(paths):
        print(f"Path {path_idx}: {path}")

        health_list = [grid[row][col][0] for row, col in path]
        gold_list = [grid[row][col][1] for row, col in path]

        current_hp = STARTING_HP
        current_gold = 0
        for idx, _ in enumerate(health_list):
            current_hp += health_list[idx]
            if current_hp <= 0:
                print(f"Path {path_idx} is invalid. RIP in peace, died with HP: {current_hp} gold: {current_gold}")
                break
            current_gold += gold_list[idx]

        print(f"Starting HP: {STARTING_HP}")
        print(f"Health modifiers encountered: {health_list}")
        print(f"Gold modifiers encountered: {gold_list}")
        print(f"Max possible gold: {sum(gold_list)}")
        print(f"Finishing HP: {current_hp}")
        print(f"Finishing gold: {current_gold}")
        print()
        results_so_far.append((path_idx, current_gold))

    results_so_far.sort(key=lambda x: x[1], reverse=True)
    return results_so_far[0][0], results_so_far[0][1]


if __name__ == "__main__":
    combined_map = combine_maps(DUNGEON_MAP, GOLD_MAP)

    all_valid_paths = find_all_paths(DUNGEON_MAP)
    idx, gold = find_best_solution(combined_map, all_valid_paths)

    print("-" * 20 + " SOLUTION " + "-" * 20)
    print(f"Best path: #{idx}")
    print(f"Best path gold sum: {gold}")
