def matrix_addition(a, b):
    #create empty array to store output
    sum = []
    #list compression
    sum = [[a[x][y] + b[x][y] for y in range(len(b))] for x in range(len(a))]
    #sum variable is the addition of the numbers at equal positions for the range of all of them (whole matrix)
    return sum

#IN-CLASS CODE
def matrix (a,b):
	for n in range(len(a)):
		for n in range(len(a[0])):
			b[n][n] = a[n][n] + b[n][n]
	return n 
x = [1,2,3]. [3,6,8]
y = [7,2,9]. [2,4,5]
print(matrix(x,y))
