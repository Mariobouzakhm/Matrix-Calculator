# Matrix-Calculator

Matrix Calculator is a program that runs through the console and where you can perform multiple Matrix operations.

# Usage

For using the Matrix class in another project:

```python
from Matrix import Matrix

#Creates a 3x3 Matrix A with the values 1 through 9
A = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Create a 3x3 Matrix B with values 10 through 19
B = Matrix(3, 3, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])

#Performs Matrices addition
C = A.addition(B)

#Performs Matrices multiplication
D = A.matricesmult(B)

```

# Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to create/update tests as appropriate.
