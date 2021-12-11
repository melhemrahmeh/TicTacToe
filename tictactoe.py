import random


def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end=' ')
        print("\n")


def emptycells(grid):
    emptycells = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '_':
                n = (i, j)
                emptycells.append(n)
    return emptycells


def PlayerWin(grid, player):
    cnt = 0
    cnt1 = 0

    '''   x _ _
          _ x _
          _ _ x       '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == j and grid[i][j] == player:
                cnt = cnt + 1

    '''   _ _ x
          _ x _
          x _ _       '''
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1, -1, -1):
            if (len(grid) - 1) - i == j and grid[i][j] == player:
                cnt1 = cnt1 + 1

    if cnt == 3:
        return True

    if cnt1 == 3:
        return True

    # Any Horizontal tie
    for i in range(len(grid)):
        n = 0
        for j in range(len(grid[i])):
            if grid[i][j] == player:
                n += 1
        if n == 3:
            return True

    # Any vertical tie win
    for i in range(len(grid)):
        l = 0
        for j in range(len(grid)):
            if grid[j][i] == player:
                l += 1
        if l == 3:
            return True

    return False


def PCwin(grid, pc):
    cnt = 0
    cnt1 = 0

    '''   x _ _
          _ x _
          _ _ x       '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == j and grid[i][j] == pc:
                cnt = cnt + 1

    if cnt == 3:
        return True

    '''   _ _ x
          _ x _
          x _ _       '''
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1, -1, -1):
            if (len(grid) - 1) - i == j and grid[i][j] == pc:
                cnt1 = cnt1 + 1

    if cnt == 3:
        return True

    if cnt1 == 3:
        return True

    # Any Horizontal tie
    for i in range(len(grid)):
        horizontal = 0
        for j in range(len(grid[i])):
            if grid[i][j] == pc:
                horizontal = horizontal + 1
        if horizontal == 3:
            return True

    # Any Vertical tie
    for i in range(len(grid)):
        vertical = 0
        for j in range(len(grid)):
            if grid[j][i] == pc:
                vertical = vertical + 1
        if vertical == 3:
            return True

    return False


# to get the user pick from the command line
def get_user_pick(empty_cells, grid):
    lst = []
    y = input().strip()
    for i in y:
        if i != " ":
            lst.append(int(i))

    y = tuple(lst)
    if y in empty_cells:
        grid[y[0]][y[1]] = player
        return True
    else:
        return False


def computer_pick(empty_cells, grid):
    y = random.sample(empty_cells, 1)
    y = y[0]
    grid[y[0]][y[1]] = pc


def tictactoe():
    grid = []
    for i in range(3):
        grid1 = []
        for j in range(3):
            grid1.append("_")
        grid.append(grid1)

    print("Do you want o or x?")
    y = input()
    global pc
    global player

    if y == 'o':
        player = 'o'
        pc = 'x'
    else:
        player = 'x'
        pc = 'o'

    print_grid(grid)
    print()
    print("Start:")
    while True:
        print()
        if not get_user_pick(emptycells(grid), grid):
            print()
            print("Try Again :|")
            print()
            print_grid(grid)
            continue

        if PlayerWin(grid, player):
            print_grid(grid)
            print("You won!")
            break

        if not emptycells(grid):
            print_grid(grid)
            print("Tie :|")
            break

        computer_pick(emptycells(grid), grid)

        if PCwin(grid, pc):
            print_grid(grid)
            print("You lose :(")
            break

        if not emptycells(grid):
            print_grid(grid)
            print("Tie :|")
            break

        print_grid(grid)


if __name__ == '__main__':
    tictactoe()