"""
File: tokens.py
Project 7.5

Adds ^ operator for exponentiation.
Tokens for processing expressions.

Reuse your solution from Programming Exercise 7.4 as your starter file
"""

class Token(object):

	# Reuse your solution from Programming Exercise 7.4 as your starter file

    UNKNOWN  = 0        # unknown

    PLUSMIN = 1
    MULDIV = 2   
    EXPO = 3

    INT      = 4        # integer
            
    MINUS    = 5        # minus    operator
    PLUS     = 6        # plus     operator
    MUL      = 7        # multiply operator
    DIV      = 8        # divide   operator
    
    FIRST_OP = 5        # first operator code

    def __init__(self, value):
        if type(value) == int:
            self.type = Token.INT
        else:
            self.type = self.makeType(value)
        self.value = value

    def isOperator(self):
        return self.type >= Token.FIRST_OP

    def __str__(self):
        return str(self.value)
    
    def getType(self):
       return self.type
    
    def getValue(self):
       return self.value

    def makeType(self, ch):
        if   ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        else:           return Token.UNKNOWN

    def getPrecedence(self):
        """Returns the precedunce level of an operator."""
        if self.getType() in (Token.MUL, Token.DIV):
            return Token.MULDIV
        elif self.getType() in (Token.PLUS, Token.MINUS):
            return Token.PLUSMIN
        elif self.value == '^':
            return Token.EXPO



def main():
    # A simple tester program
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    unknown = Token("#")
    anInt = Token(34)
    print(plus, minus, mul, div, unknown, anInt)

if __name__ == '__main__': 
    main()
