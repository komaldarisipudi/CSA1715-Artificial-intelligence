def clean(floor):
    for i in range(len(floor)):
        if i % 2 == 0:
            for j in range(len(floor[i])):
                if floor[i][j] == 1:
                    print(f"Location ({i}, {j}) is dirty. Cleaning...")
                    floor[i][j] = 0
                else:
                    print(f"Location ({i}, {j}) is clean.")
        else:
            for j in range(len(floor[i])-1, -1, -1):
                if floor[i][j] == 1:
                    print(f"Location ({i}, {j}) is dirty. Cleaning...")
                    floor[i][j] = 0
                else:
                    print(f"Location ({i}, {j}) is clean.")
    print("Floor is clean now.")

# Test the program
floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]
clean(floor)
