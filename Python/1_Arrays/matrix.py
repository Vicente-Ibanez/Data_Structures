"""
File: matrix.py
Project 4.7

Defines a matrix class to support simple matrix arithmetic.
"""

# Write your code below:
from grid import Grid
class Matrix(object):
    def __init__(self, rows, columns, fillValue=None) -> None:
        self.matrix = Grid(rows, columns, fillValue)
    
    def __add__(self, m2):
        sum = Grid(
            self.matrix.getHeight(),
            self.matrix.getWidth()
        )
       
        for row in range(self.matrix.getHeight()):
            for column in range(self.matrix.getWidth()):
                sum[row][column] = self.matrix[row][column] +  m2.matrix[column][row]
        return sum

    def __sub__(self, m2):
        sum = Grid(
            self.matrix.getHeight(),
            self.matrix.getWidth()
        )
       
        for row in range(self.matrix.getHeight()):
            for column in range(self.matrix.getWidth()):
                sum[row][column] = self.matrix[column][row] -  m2.matrix[column][row]
       
        return sum

    def __mul__(self, m2):
        if self.matrix.getWidth() != m2.matrix.getHeight():
            raise Exception
        
        mul = Grid(
            self.matrix.getHeight(),
            m2.matrix.getWidth(),
            0
        )
       
        for row in range(self.matrix.getHeight()):
            for col in range(m2.matrix.getWidth()):
                for column in range(self.matrix.getWidth()):
                    mul[row][col] += self.matrix[row][column] *  m2.matrix[column][col]
        return mul


def main():
    m1 = Matrix(3, 3, 2)
    m2 = Matrix(3, 3, 4)
    print(m1 + m2)
    m1 = Matrix(4, 4, 2)
    m2 = Matrix(4, 4, 4)
    print(m2 - m1) 
    m1 = Matrix(2, 3, 2)
    m2 = Matrix(3, 2, 4)
    print(m1 * m2) 

if __name__ == "__main__": main()