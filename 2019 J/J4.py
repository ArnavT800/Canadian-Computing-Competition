f = input()
grid = [1, 2, 3, 4]
for i in f:
    if i == "H":
        grid[0], grid[2] = grid[2], grid[0]
        grid[1], grid[3] = grid[3], grid[1]
    else:
        grid[0], grid[1] = grid[1], grid[0]
        grid[2], grid[3] = grid[3], grid[2]

print(grid[0], grid[1])
print(grid[2], grid[3])
