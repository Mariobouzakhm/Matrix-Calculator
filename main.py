#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mario Bouzakhm
Date: 06-2020

Matrix Calculator Interface
"""

from Matrix import Matrix


def printmenu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')


def printtransposeoptions():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Verical line')
    print('4. Horizontal line')


def matrixinput(order='', func=float):
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

    while True:
        printmenu()

        cmd = input('Your choice: ')

        if cmd == '1':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = A.addition(B)
            C.displaymatrix()

        elif cmd == '2':
            A = matrixinput()
            constant = float(input('Enter constant: '))

            B = A.constantmult(constant)
            B.displaymatrix()

        elif cmd == '3':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = A.matricesmult(B)
            C.displaymatrix()

        elif cmd == '4':
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

        elif cmd == '5':
            A = matrixinput()
            det = A.determinant()

            print('The result is: ')
            print(str(det))

        elif cmd == '6':
            A = matrixinput()
            B = A.inverse()

            B.displaymatrix()

        elif cmd == '0':
            break

        print("")


main()





