#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mario Bouzakhm
Date: 06-2020

Class that represents a Matrix in mathematics.
"""


class Matrix:
    def __init__(self, rows, columns, values):
        """
        Constructor of the class

        rows: int, number of rows of the matrix
        columns: int, number of columns of thr matrix
        values: double nested lists, containing the values of the matrix
        """

        self.rows = rows
        self.columns = columns
        self.values = values

    @staticmethod
    def getidentitymatrix(size):
        """
        An identity matrix is a aquare matrix whose values are zero except for the ones along the main diagonal.

        size: int, size of the identity matrix to return

        Returns an identity matrix of the specified size.
        """

        if size <= 0:
            print("This operation cannot be performed.")
            return

        result = []

        for i in range(size):
            line = []
            for j in range(size):
                if i == j:
                    line.append(1)
                else:
                    line.append(0)

            result.append(line)

        return Matrix(size, size, result)

    @staticmethod
    def dotproduct(list1, list2):
        """
        The dot product of two lists, is the addition of the product of the correponding elements of the two lists.

        list1, list
        list2, list

        Returns the dot product of the two lists.
        """
        if len(list1) != len(list2):
            return 'ERROR'
        else:
            sum = 0

            for i in range(len(list1)):
                sum += (list1[i] * list2[i])

            return sum

    def displaymatrix(self):
        """
        Displays the matrix to the console in a table-like structure.
        """
        print('The result is: ')
        for i in range(self.rows):
            for j in range(self.columns):
                print(str(self.values[i][j]) + " ", end='')
            print("\n", end='')

    def gettruncatedmatrix(self, row, column):
        """
        A truncated matrix, is the matrix held by the Matrix instance
        but removing a values along a row and column of the matrix.

        row, int
        column, int

        Returns a truncated matrix along the row/column specified originated from the Matrix instance.
        """
        if self.rows < row or self.columns < column or row <= 0 or column <= 0:
            print('This operation cannot be performed.')
            return

        result = [[self.values[i][j] for j in range(self.columns)] for i in range(self.rows)]
        del(result[row - 1])

        for i in range(len(result)):
            del(result[i][column - 1])

        return Matrix(self.rows - 1, self.columns - 1, result)

    def getverticallist(self, colnum):
        """
        A vertical list in this program refers to the values from the Matrix instance alongside a column.

        colnum, int

        Returns a list of the values of the column specified from the Matrix.
        """
        if colnum > self.rows:
            return 'ERROR'

        col = []
        for i in range(self.rows):
            col.append(self.values[i][colnum])

        return col

    def cofactormatrix(self):
        """
        Returns a Matrix of the containing the cofactor of each element of the matrix.
        The cofactor of an element in a matrix, is a complex operation.

        It is calculated using the following forumla: C = (-1)**(i+j) * M(i, j)
        Where i and j are the indexes of the element and M is the minor of the element,
        which is the determinant of the matrix obtained by truncating the original matrix along the row i and column j.
        """
        if not self.__issquare():
            print('This operation cannot be performed')
            return

        result = []

        for i in range(self.rows):
            line = []
            for j in range(self.columns):
                line.append((((-1)**(i+j)) * self.gettruncatedmatrix(i + 1, j + 1).determinant()))

            result.append(line)

        return Matrix(self.rows, self.columns, result)

    def addition(self, B):
        """
        B, Matrix

        Returns a matrix represeting the addition of the Matrix instance and the Matrix B.
        Only possible if both matrices have the same size.
        Matrices Addition is obtained by calculating the sum of each correpsonding pair of elements for each matrix and
        placing them in the result matrix.
        """

        if not isinstance(B, Matrix) or (self.rows != B.rows or self.columns != B.columns):
            print("This operation cannot be performed.")
        else:
            resultMatrix = []

            for i in range(self.rows):
                resultingLine = []
                for j in range(self.columns):
                    sum = self.values[i][j] + B.values[i][j]
                    resultingLine.append(sum)

                resultMatrix.append(resultingLine)

            return Matrix(self.rows, self.columns, resultMatrix)

    def subtract(self, B):
        """
        B, Matrix

        Returns a matrix represeting the subtraction of the Matrix instance and the Matrix B.
        Only possible if both matrices have the same size.
        For details, on subtraction of matrices refer to the method above, same principle but by subtracting the numbers
        """
        if not isinstance(B, Matrix) or (self.rows != B.rows or self.columns != B.columns):
            print("This operation cannot be performed.")

        else:
            B = B.constantmult(-1)
            return self.addition(B)

    def constantmult(self, constant):
        """"
        constant, real number

        Returna a matric represeting the constant multiplication of the Matrix instance by the number constant.
        The result Matrix is obtained by multiplying each element of the initial matrix by the constant.
        """
        resultMatrix = []

        for i in range(self.rows):
            resultingLine = []

            for j in range(self.columns):
                resultingLine.append(constant * self.values[i][j])

            resultMatrix.append(resultingLine)

        return Matrix(self.rows, self.columns, resultMatrix)

    def matricesmult(self, B):
        """
        B, Matrix

        Return the matrix obtained by multiplying the Matrix instance (A) by B. (Operation AxB)
        Only possible if the number of columns of A equals the number of rows of B.
        The process of matrices multiplication is too complex to be explained here.
        Check the following site: https://www.mathsisfun.com/algebra/matrix-multiplying.html
        """

        if not isinstance(B, Matrix) or (self.columns != B.rows):
            print("This operation cannot be performed")
        else:
            result = []

            for i in range(self.rows):
                resultLine = []

                list1 = self.values[i]
                for j in range(B.columns):
                    list2 = B.getverticallist(j)

                    sum = Matrix.dotproduct(list1, list2)

                    resultLine.append(sum)

                result.append(resultLine)

            return Matrix(self.rows, B.columns, result)

    def maindiagonaltranspose(self):
        """
        Returns the Matrix obtained when we transpose the Matrix instance along the main diagonal.
        A transposed Matrix is denoted A^(T) for a matrix A.
        Check the following site: https://www.mathsisfun.com/definitions/transpose-matrix-.html
        """
        result = []

        for i in range(self.columns):
            line = self.getverticallist(i)

            result.append(line)

        return Matrix(self.columns, self.rows, result)

    def sidediagonaltranspose(self):
        """
        Returns the Matix obtained when we transpose the Matrin instance along the side diagonal.
        Same procedure as the method above, but using the other diagonal.
        """
        result = []

        for i in range(self.columns - 1, -1, -1):
            line = self.getverticallist(i)
            line.reverse()

            result.append(line)

        return Matrix(self.columns, self.rows, result)

    def verticaltranspose(self):
        """
        Returns the Matrix obtained when we transpose the Matrin instance vertically.
        Meaning the result Matrix is obtained by reflecting the initial Matrix along its middle vertical point.
        Ex:
        | 1 2 |    | 2 1 |
        | 3 4 | -> | 4 3 |
        | 5 6 |    | 6 5 |
        """
        if self.columns == 1:
            return self

        i = 0
        j = self.columns - 1

        if self.columns % 2 == 0:
            result = [[0 for __ in range(self.columns)] for _ in range(self.rows)]
        else:
            middle = self.columns // 2
            result = []
            for k in range(self.rows):
                line = []
                for l in range(self.columns):
                    if l == middle:
                        line.append(self.values[k][l])
                    else:
                        line.append(0)

                result.append(line)

        while i < j:
            for k in range(self.rows):
                value1 = self.values[k][i]
                value2 = self.values[k][j]

                result[k][j] = value1
                result[k][i] = value2

            i += 1
            j -= 1

        return Matrix(self.rows, self.columns, result)

    def horizontaltranspose(self):
        """
        Returns the Matrix obtained when we transpose the Matrin instance horizontally.
        Meaning the result Matrix is obtained by reflecting the initial Matrix along its middle horizontal point.
        Ex:
        | 1 2 3 |    | 4 5 6 |
        | 4 5 6 | -> | 1 2 3 |
        """
        if self.rows == 1:
            return self

        i = 0
        j = self.rows - 1

        result = self.values[:]

        while i < j:
            result[i] = self.values[j]
            result[j] = self.values[i]

            i += 1
            j -= 1

        return Matrix(self.rows, self.columns, result)

    def determinant(self):
        """
        The determinant of a Matrix is a number used in a variety of matrix operations (Matrix Inverses...)
        It is denoted det(A) for a Matrix A.
        The determinant of a Matrix can only be calculated for square matrices.

        The determinant of a 1x1 matrix is the only element itself.
        The process of calculating the determinant of a matrix is complicated and includes recursion.
        Check the following site: https://www.mathsisfun.com/algebra/matrix-determinant.html

        Returns the determinant of the Matrix instance.
        """
        if not self.__issquare():
            print('This operation cannot be performed.')
            return

        if self.rows == 1:
            return self.values[0][0]

        if self.rows == 2:
            return (self.values[0][0] * self.values[1][1]) - (self.values[0][1] * self.values[1][0])

        det = 0
        for j in range(self.columns):
            det += (((-1)**j) * self.values[0][j] * self.gettruncatedmatrix(1, j + 1).determinant())

        return det

    def inverse(self):
        """
        The Inverse of a Matrix A is denotated as A^(-1) and is defined by AA^(-1)=A^(-1)A=I

        It is only possible to calculate the inverse of a square matrix whose determinant is not zero.
        The operation to calculate the inverse is:

        A^(-1) = 1/det(A) * C^(T)
        - det(A) is the determinant of A
        - C is the cofactor Matrix of A
        - C^(T) is the cofactor Matrix of A transposed along its main diagonal.

        Returns the inverse of the instance Matrix.
        """

        if not self.__issquare():
            print('This operation cannot be performed.')
            return

        det = self.determinant()
        if det == 0:
            print('This operation cannot be performed.')
            return

        cofactor = self.cofactormatrix().maindiagonaltranspose()
        result = cofactor.constantmult(1/det)

        return result

    def __issquare(self):
        """
        A Square Matrix is a matrix which have the same number of rows and columns.

        Returns True if the Matrix instance is a Square matrix, False otherwise.
        """
        return self.rows == self.columns






