matrix=[
    [9,2,3],
    [4,7,6],
    [8,1,4]
] 
smallest =matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]<smallest:
            smallest=matrix[i][j]
print(smallest)            
  