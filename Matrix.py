class Matrix:
    def __init__(self, rows, columns, values):
        self.rows = rows
        self.columns = columns
        self.values = values

    @staticmethod
    def getidentitymatrix(size):
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
        if len(list1) != len(list2):
            return 'ERROR'
        else:
            sum = 0

            for i in range(len(list1)):
                sum += (list1[i] * list2[i])

            return sum

    def displaymatrix(self):
        print('The result is: ')
        for i in range(self.rows):
            for j in range(self.columns):
                print(str(self.values[i][j]) + " ", end='')
            print("\n", end='')

    def gettruncatedmatrix(self, row, column):
        if self.rows < row or self.columns < column or row <= 0 or column <= 0:
            print('This operation cannot be performed.')
            return

        result = [[self.values[i][j] for j in range(self.columns)] for i in range(self.rows)]
        del(result[row - 1])

        for i in range(len(result)):
            del(result[i][column - 1])

        return Matrix(self.rows - 1, self.columns - 1, result)

    def getverticallist(self, colnum):
        if colnum > self.rows:
            return 'ERROR'

        col = []
        for i in range(self.rows):
            col.append(self.values[i][colnum])

        return col

    def cofactormatrix(self):
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

    def constantmult(self, constant):
        resultMatrix = []

        for i in range(self.rows):
            resultingLine = []

            for j in range(self.columns):
                resultingLine.append(constant * self.values[i][j])

            resultMatrix.append(resultingLine)

        return Matrix(self.rows, self.columns, resultMatrix)

    def matricesmult(self, B):

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
        result = []

        for i in range(self.columns):
            line = self.getverticallist(i)

            result.append(line)

        return Matrix(self.columns, self.rows, result)

    def sidediagonaltranspose(self):
        result = []

        for i in range(self.columns - 1, -1, -1):
            line = self.getverticallist(i)
            line.reverse()

            result.append(line)

        return Matrix(self.columns, self.rows, result)

    def verticaltranspose(self):
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
        return self.rows == self.columns






