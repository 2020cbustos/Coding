def matrix_addition(a, b):
    #create empty array to store output
    sum = []
    #list compression
    sum = [[a[x][y] + b[x][y] for y in range(len(b))] for x in range(len(a))]
    #sum variable is the addition of the numbers at equal positions for the range of all of them (whole matrix)
    return sum
