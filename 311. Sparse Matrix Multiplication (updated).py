

'''
311. Sparse Matrix Multiplication
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [[ 1, 0, 0], [-1, 0, 3]]
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

A(n,k) %*% B(k,m) = C(n,m) = |A_row1 %*% B_col1, A_row1 %*% B_col2, A_row1 %*% B_col3|
                             |A_row2 %*% B_col1, A_row2 %*% B_col2, A_row3 %*% B_col3|
                         
where A_row1 %*% B_col1 = A11* B11 + A12* B21 + A13*B31 

solution: 
use hashmap to store non-zero rows and columns in A, and B (a row is non-zero row if all elements are non-zero) 
initialize a result matrix with dimension (n,m), and all values = 0 
update this matrix use 
Complexity time(worse case) O(n*n*m), space O(n*m)
'''

class Matrix: 
    def mult(self, A, B): 
        if not A or not B: return [[]]
        n, k = len(A), len(A[0])
        m = len(B[0])
        mapA = {(i, j): A[i][j] for i in range(n) for j in range(k) if A[i][j]} 
        mapB = {(i, j): B[i][j] for i in range(k) for j in range(m) if B[i][j]} 
        C = [[0]*m for _ in range(n)]
        for i, j in mapA.keys():   #mapA = {(0,0):1, (1,0):-1, (1,2): 3},  mapB ={(0,0):7, (2,2):1}
            for x, y in mapB.keys(): 
                if j == x: 
                    C[i][y] += mapA[i,j] * mapB[x,y]
        return C 
A = [[ 1, 0, 0], [-1, 0, 3]]
B = [[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]
            
t = Matrix()
C = t.mult(A, B)
print(C)      
        
        
        
