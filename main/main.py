#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mario Bouzakhm
Date: 06-2020

Matrix Calculator Interface
"""

from Matrix import Matrix

def printmenu():
    """
    Displays  the matrix calculator options.
    """
    print('1. Add matrices')
    print('2. Subtract matrices')
    print('3. Multiply matrix by a constant')
    print('4. Multiply matrices')
    print('5. Transpose matrix')
    print('6. Calculate a determinant')
    print('7. Inverse matrix')
    print('8. Matrix Powers')
    print('0. Exit')


def printtransposeoptions():
    """
    Displays the matrix transpose options.
    """
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Verical line')
    print('4. Horizontal line')


def matrixinput(order='', func=float):
    """
    Prompts the user to enter a Matrix

    order: str, which represent the number of the matrix to be entered for clarity (ex. first, second...)
    func: function, which represents how the matrix values are read (int for integer matrix, float for matrix with decimals)

    Returns an instance of the Matrix Class.
    """
    dimensions = [int(x) for x in input("Enter size of " + order + " matrix: ").strip().split(" ")]
    A = []
    print('Enter ' + order + ' matrix: ')
    for i in range(dimensions[0]):
        numbers = [func(x) for x in input().split(" ")]
        while len(numbers) != dimensions[1]:
            print("Invalid Numbers.")
            numbers = [func(x) for x in input().split(" ")]

        A.append(numbers)

    return Matrix(dimensions[0], dimensions[1], A)


def main():
    """
    Main Program Execution. Will prompt the user for the matrix calculater options.
    Proceed to make the operation/calculations.
    """

    while True:
        printmenu()

        cmd = input('Your choice: ')

        if cmd == '1':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = A.addition(B)
            C.displaymatrix()

        elif cmd == '2':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = A.subtract(B)
            C.displaymatrix()

        elif cmd == '3':
            A = matrixinput()
            constant = float(input('Enter constant: '))

            B = A.constantmult(constant)
            B.displaymatrix()

        elif cmd == '4':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = A.matricesmult(B)
            C.displaymatrix()

        elif cmd == '5':
            print('')
            printtransposeoptions()

            cmd2 = input('Your choice: ')

            if cmd2 == '1':
               A = matrixinput()
               B = A.maindiagonaltranspose()

               B.displaymatrix()

            elif cmd2 == '2':
                A = matrixinput()
                B = A.sidediagonaltranspose()

                B.displaymatrix()
            elif cmd2 == '3':
                A = matrixinput()
                B = A.verticaltranspose()

                B.displaymatrix()
            elif cmd2 == '4':
                A = matrixinput()
                B = A.horizontaltranspose()

                B.displaymatrix()

        elif cmd == '6':
            A = matrixinput()
            det = A.determinant()

            print('The result is: ')
            print(str(det))

        elif cmd == '7':
            A = matrixinput()
            B = A.inverse()

            B.displaymatrix()

        elif cmd == '8':
            A = matrixinput()
            power = int(input('Enter power: '))

            B = A.pow(power)
            B.displaymatrix()

        elif cmd == '0':
            break

        print("")


main()





