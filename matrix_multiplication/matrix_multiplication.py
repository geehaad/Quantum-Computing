import sys

def get_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end = " ")
        print(end = "\n")
    

def create_matrix(R, C):
    matrix = []
    print("Enter the entries column-wise:")
    for i in range(R): #Row iteration
        rowList=[]
        for j in range(C): #Column iteration
            rowList.append(int(input()))
        matrix.append(rowList)
    return matrix

def cmp_mult(matrixA, matrixB):
    matrixC = [([0]*len(matrixB[0])) for i in range(len(matrixA))]
    for i in range(len(matrixA)): # iterat through rows of A
        for j in range(len(matrixB[0])): # iterat through columns of B
            for k in range(len(matrixB)): #iterate through  raws of B
                matrixC[i][j] +=matrixA[i][k]*matrixB[k][j]
    print("The multiplication matrix is")
    return matrixC

def trans(matrix):
    trans_matrix = [([0]*len(matrix)) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


if __name__ == '__main__':
    RA = int(input("Enter the number of rows of the first matrix:"))
    CA = int(input("Enter the number of columns of the first matrix:"))
    matrixA = create_matrix(RA, CA)
    print("The matrix A is:")
    get_matrix(matrixA)
    print("**********")
    RB = int(input("Enter the number of rows of the second matrix:"))
    CB = int(input("Enter the number of columns of the second matrix:"))
    matrixB = create_matrix(RB, CB)
    print("The matrix B is:")
    get_matrix(matrixB)
    f = int(input("Do you want Classical:1 ,or Quantum:0 operation : "))
    if(f==1):
        if(CA != RB):
            print("Envalid operation: The number of columns of the first matrix must equal the number of columns in the second matrix")
            sys.exit()
        ans = cmp_mult(matrixA,matrixB)
        get_matrix(ans)
    else:
        if(CA == RB):
            print("Envalid operation: The number of columns of the first matrix must equal the number of columns in the second matrix")
            sys.exit()
        matrixB_trans= trans(matrixB)
        ans_Qua = cmp_mult(matrixA,matrixB_trans)
        get_matrix(ans_Qua)







    

    
    

    
        
        
   
