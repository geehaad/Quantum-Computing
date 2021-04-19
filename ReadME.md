<body style="font-size:22px">
<h1>Quantum  Computing</h1>

<div>
Outline:

<ul>
<li>Schrödinger's cat
</li>
<li>Quantum computer
</li>
<li>Basic operations
</li>
</ul>

<h1>Schrödinger's cat</h1>
</ul>
</div>

<div>
<img src="matrix_multiplication/cat.jpg" width="400px" style="float:left"><br>
<p >
You probably heard before about the Schrödinger's cat, Schrödinger's cat is a thought experiment that asks a question, is the cat, which is inside a box, alive or dead?<br>
Let's imagine you opened the box at time x-1, and you found the cat is alive, now you think that the cat is always alive,<br>
but what if you opened the box at time x+1, and found that the cat is dead!!<br>
know you know definitely that the car is alive at time x-1 and dead at time x+1, but what is her situation at time x?<br>
In the thought experiment, a hypothetical cat may be considered simultaneously both alive and dead as a result of being linked to a random subatomic event that may or may not occur. <br>
</p><br>
<br><br>
</div>
<h1>Quantum computer</h1>
<p >
The experiment we viewed before is the main idea of the quantum computer.<br>
In normal computers, which we use nowadays, and are also known as classical computers, the data, or the bit, is either 0 or 1, on or of, it cannot be both, <br>
that gives us one out of 2 to the power N possible permutations.<br>
But by the quantum data, which is also known as a qubit, can be both 0 and 1 with All of 2 to the power N possible permutations.<br>
</p>

<h1>Basic operation</h1>
<p >
<div>
Now we will see some linear algebra operation in classical computer and quantum computer:<br>
</div>
<h1>Matrix multiplication</h1>

<h2 >Definition</h2>
<p >In mathematics, particularly in linear algebra, <span style="color:yellow">matrix multiplication</span> <br>
is a binary operation that produces a matrix from two matrices. <br>
For <span style="color:yellow">matrix multiplication</span>, the number of columns in the first matrix must be equal to the number of rows in the second matrix.<br>
 The resulting matrix, known as the matrix product, has the number of rows of the first and the number of columns of the second matrix. <br>
 The product of matrices A and B is denoted as AB. <br>
 <div>From Wikipedia, the free encyclopedia</div></p> 


<h2>How can we do this?</h2>
<p>Let's Define matrix A  with size: m X k ,and matrix B with size: k X n <br>
<img src="matrix_multiplication/matrix.png" width="540px"><br>
<br>
Then, as we saw in the definition, the number of columns in A is equal to the number of columns in B, then the multiplication, AB, can be done by the following approach:<br>
<br>
We consider multiplying the rows of the first matrix with the opposite columns of the second matrix.<br>
 <img src="matrix_multiplication/matrix_multiplication.png" width="400px" >

<h3>Steps: </h3>

We multiply the first element in the first row in the first matrix, A, with the first element of the first column in the second matrix, B, we also call this <span style="color:blue">dot notation</span><br>,<br>
we still in the same row of A, and the same column of B, we add the previous multiplication to the second multiplication, <br>
the second multiplication is multiplying the second element in the first row in the first matrix, A, with the second element of the first column in the second matrix, <br>
until the end of the row and the column <small>-remember that the number of columns of the first matrix is equal to the number of rows of the second matrix-</small> <br>
then we move to the second row of A and the second column of B and apply the same approach till the end of the two matrics.<br>

<div style=" text-align: center;">
<img src="matrix_multiplication/what.jpg" width="450px" ><br>
</div>


Well, This is alot of talking, let's write it in beutiful notations:<br>

<img src="matrix_multiplication/multi.gif" width="650px">

1- Let's consider the output matrix is C, we know that the first ever element:<br>
in A: A[0][0], and in B: B[0][0],<br>
we multiply them in put the answer in the first element in C:<br>
C[0][0] = A[0][0].B[0][0]<br>
2- The second element in the same row of A: a[0][1] and same column of B: b[1][0], <br>
as we still in the same row of A, we add this in the same element of C:<br>
C[0][0] += A[0][1].B[1][0],<br>

Do you get the equation? <br>

let's take another row of A:<br>
3- Consider we moved to the second row of A [1][0], and the second column of B[0][1]:<br>
remember the row of C is as the row of A, and the column of C is as B:<br>
C[1][0] = A[0][1].B[0][0]<br>

at the end C is looking like that:<br>
<img src="matrix_multiplication/c.png"><br>

Now we are ready to write the formal equation:<br>

C[i][j]= A[i][0].B[0][j]+ A[i][1].B[1][j]+ ... +A[i][n].B[n][j]<br>

<p>

<h1>Implement the outer product:</h1>
We Will see how to write the code in python:<br>
<ul>
<li>nested for loop <br>
With : O(n^3) <br>

</li>
<li><pre>for i in range(len(matrixA)): # iterat through rows of A
            for j in range(len(matrixB[0])): # iterat through columns of B
                for k in range(len(matrixB)): #iterate through  raws of B
                    matrixC[i][j] += matrixA[i][k]*matrixB[k][j]</li>
    </pre>                

<p> The main idea here is to iterate over the rows of the first matrix and the columns of the second matrix,then apply the function we produce before.</p><br>

</ul>

</p>

<h2>Quantum computer</h2>
<p>
as we did before in classical linear algebra, the multiplication is the same, but it differes in that we get the transpose of the second matrix,<br>
we will use the vectore|matrix notation<br>
let's get the transpose of the matrix:<br>
<pre>
def trans(matrix):<br>
    trans_matrix = [([0]*len(matrix)) for i in range(len(matrix[0]))]<br>
    for i in range(len(matrix)):<br>
        for j in range(len(matrix[0])):<br>
            trans_matrix[j][i] = matrix[i][j]<br>
    return trans_matrix<br>
</pre>
</p>
<div style=" text-align: center;"> <img src="matrix_multiplication/giphy.gif" width="500px"></div>
</p>

</body>
