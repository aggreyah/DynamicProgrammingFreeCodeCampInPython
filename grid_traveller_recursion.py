def grid_traveller(m, n):
    if(m == 0 or n == 0):
        return 0
    elif(m == 1 and n == 1):
        return 1
    else:
        return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)

if __name__ == "__main__":
    print(grid_traveller(18, 18))