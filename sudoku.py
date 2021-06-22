def is_valid(grid,guess,row,column):
    #row check
    # here we check for all the row values by first storing
    # in row_vals and if the guess is already present
    # we return false and look for next guess
    row_vals=grid[row]
    if guess in row_vals:
        return False
    # column check
    # here we make list of column values and check
    # if the guess is present in list
    # if it is we return false and look
    # for next guess no
    col_vals=[]
    for i in range(9):
        col_vals.append(grid[i][column])
    if guess in col_vals:
        return False

    # here we are checking in a 3x3 box
    # 0 to 2 one colbox 3 to 5 2nd col box and 6 to 8
    # 3rd col box if we see horizontally
    # we go same for rol box vertically
    # after checking for rows and cols we check in 3x3
    # box if guess is already present we return false
    # and look for next guess no.
    rowbox=(row//3)*3
    colbox=(column//3)*3
    for a in range(rowbox,rowbox+3):
        for b in range(colbox,colbox+3):
            if grid[a][b]==guess:
                return False
    return True


def find_empty(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column]==0:
                return row,column
    return None,None

def solve(grid):
    # we are finding all the empty cells in the grid
    # and if there is no empty cells we return true
    row,column=find_empty(grid)
    if row is None:
        return True

    # we place the values 1 to 9 to check see
    # if the guess is valid or not
    for guess in range(1,10):
        if is_valid(grid,guess,row,column):
            grid[row][column]=guess
            # now using this puzzle we recursively solve call solve
            if solve(grid):
                return True
        # if the guess is not valid or our guess doesnt solve the we backtrack and try new guess
        grid[row][column]=0

    return False





grid=[]
for i in range(9):
    a=list(map(int,input().split()))
    grid.append(a)
print(solve(grid))
for i in range(9):
    for j in range(9):
        print(grid[i][j],end=" ")
    print()

