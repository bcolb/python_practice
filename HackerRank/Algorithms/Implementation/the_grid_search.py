def get_grid(row_count, column_count):
    row_list = []
    for i in range(0, row_count):
        row_list.append(input())
    return row_list
    
def check_grids(grid, R, C, pattern, r, c):
    # Check for case where pattern dimensions are larger than grid dimensions
    if r > R or c > C:
        return False
    # loop through all possible sub grids
    subc = 0
    if c > 1:
        subc = c - 1
    subr = 0
    if r > 1:
        subr = r - 1
    for gc in range(0, C-subc):
        for gr in range(0, R-subr):
            # get sub grid
            for pr in range(0, r):
                all_match = True
                if pattern[pr] != grid[gr+pr][gc:gc+c]:
                    all_match = False
                    break
            if all_match:
                return True
    return False
            

def start():
    t = int(input())
    for i in range(0, t):
        grid_rc = [int(x) for x in str(input()).split(' ')]
        grid = get_grid(grid_rc[0], grid_rc[1])
        pattern_rc = [int(x) for x in str(input()).split(' ')]
        pattern = get_grid(pattern_rc[0], pattern_rc[1])
        if check_grids(grid, grid_rc[0], grid_rc[1], pattern, pattern_rc[0], pattern_rc[1]):
            print("YES")
        else:
            print("NO")

start()
