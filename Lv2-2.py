# 2. Diagonal sum of 3x3 matrix
m=[1,2,3,4,5,6,7,8,9]
diag=[m[i*3+i] for i in range(3)]
diag_sum=sum(diag)
print("Diagonal elements are", diag)
print("Sum of diagonal elements =", diag_sum)
