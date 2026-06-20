matrix=[
    [9,2,3],
    [4,7,6],
    [8,1,4]
] 
largest =matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]>largest:
            largest=matrix[i][j]
print(largest)            
            
            