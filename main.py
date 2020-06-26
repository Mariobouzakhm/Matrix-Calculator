#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mario Bouzakhm
Date: 06-2020

Matrix Calculator Interface
"""


def matrixinput():
    dimensions = [int(x) for x in input("Enter the dimension of the matrix: ").strip().split(" ")]
    A = []
    for i in range(dimensions[0]):
        numbers = [int(x) for x in input("Enter the numbers of line " + str(i + 1) + ": ").split(" ")]
        while len(numbers) != dimensions[1]:
            print("Invalid Numbers.")
            numbers = [int(x) for x in input("Enter the numbers of line " + str(i + 1) + ": ").split(" ")]

        A.append(numbers)

    return A


def displaymatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j])+ " ", end='')
        print("\n", end='')


def additionmatrix(A, B):
    dimensions1 = [len(A), len(A[0])]
    dimensions2 = [len(B), len(B[0])]

    if dimensions1[0] != dimensions2[0] or dimensions1[1] != dimensions2[1]:
        print("ERROR")
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


A = matrixinput()
constant = int(input("Enter the constant of multiplication: "))

displaymatrix(matrixconstantmult(A, constant))





