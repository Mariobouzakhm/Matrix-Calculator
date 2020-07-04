#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mario Bouzakhm
Date: 06-2020

Matrix Calculator Interface
"""


def printmenu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')


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

    return A


def displaymatrix(matrix):
    print('The result is: ')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j])+ " ", end='')
        print("\n", end='')


def additionmatrix(A, B):
    dimensions1 = [len(A), len(A[0])]
    dimensions2 = [len(B), len(B[0])]

    if dimensions1[0] != dimensions2[0] or dimensions1[1] != dimensions2[1]:
        print("This operation cannot be performed")
    else:
        resultMatrix = []

        for i in range(len(A)):
            resultingLine = []
            for j in range(len(A[i])):
                sum = A[i][j] + B[i][j]
                resultingLine.append(sum)

            resultMatrix.append(resultingLine)

        return resultMatrix


def matrixconstantmult(A, constant):
    resultMatrix = []

    for i in range(len(A)):
        resultingLine = []

        for j in range(len(A[i])):
            resultingLine.append(constant * A[i][j])

        resultMatrix.append(resultingLine)

    return resultMatrix


def mattricesmult(A, B):
    dimensions1 = [len(A), len(A[0])]
    dimensions2 = [len(B), len(B[0])]

    if dimensions1[1] != dimensions2[0]:
        print("This operation cannot be performed.")

    else:
        result = []

        for i in range(dimensions1[0]):
            resultLine = []

            list1 = A[i]
            for j in range(dimensions2[1]):
                list2 = getverticallist(B, j)

                sum = dotproduct(list1, list2)

                resultLine.append(sum)


            result.append(resultLine)

        return result


def dotproduct(list1, list2):
    if len(list1) != len(list2):
        return 'ERROR'
    else:
        sum = 0

        for i in range(len(list1)):
            sum += (list1[i] * list2[i])

        return sum


def getverticallist(matrix, colnum):
    if colnum > len(matrix):
        return 'ERROR'

    col = []
    for i in range(len(matrix)):
        col.append(matrix[i][colnum])

    return col


def main():
    while True:
        printmenu()

        cmd = input('Your choice: ')

        if cmd == '1':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = additionmatrix(A, B)
            displaymatrix(C)

        elif cmd == '2':
            A = matrixinput()
            constant = float(input('Enter constant: '))

            B = matrixconstantmult(A, constant)
            displaymatrix(B)

        elif cmd == '3':
            A = matrixinput(order='first')
            B = matrixinput(order='second')

            C = mattricesmult(A, B)
            displaymatrix(C)

        elif cmd == '0':
            break

        print("")

main()





