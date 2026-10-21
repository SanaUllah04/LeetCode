x = 100
s = 0

grid = [[s,1,1],
        [0,1,0],
        [0,0,x]]

print(grid)
size = len(grid)
print(size)

def fewSteps(matrix):
    if not matrix:
        return -1
    
    steps = 0
    paths = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("matrix i = ", i, "Matrix J = ", j)
            if matrix[i][j] == 1:
                break

            if matrix[i][j] == 0:
                print("MATRIX VALUE = ", matrix[i][j])
                paths.append([i,j])
                steps += 1 
                print("Path = ", paths,"Steps = ",steps)

            elif matrix[i][j] == 'x':
                return steps
    return steps      


print("\n\n\nTotal Number of Steps = ",fewSteps(grid))