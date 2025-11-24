"""
File: expressiontree.py
Project 10.7  Completes the node classes for expression trees.

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self.data = data

    def postfix(self):
        return str(self)
    
    def prefix(self):
        return str(self)
    
    def infix(self):
        return str(self)
    
    def value(self):
        return self.data
    
    def __str__(self):
        return str(self.data)
    


class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self.operator = op
        self.leftOperator = leftOper
        self.rightOperator = rightOper

    def postfix(self):
        return self.leftOperator.postfix() + " " + \
        self.rightOperator.postfix() + " " + \
        str(self.operator)
    
    def prefix(self):
        return str(self.operator) + " " + \
        self.leftOperator.prefix() + " " + \
        self.rightOperator.prefix()
        
    
    def infix(self):
        return "(" + self.leftOperator.infix() + " " + \
        str(self.operator) + " " + \
        self.rightOperator.infix() + ")"
    
    def value(self):
        leftOp = self.leftOperator.value()
        rightOp = self.rightOperator.value()

        match self.operator._value:
            case "-":
                return leftOp - rightOp
            case "+":
                return leftOp + rightOp
            case "*":
                return leftOp * rightOp
            case "/":
                return leftOp / rightOp
        

    def computerValue(self):
        return self.value()

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3) - (2 + 3)):", c.infix())
    print("Expect - * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -       :", c.postfix())
    print("Expect 15                      :", c.value())

if __name__ == "__main__":
    main()




