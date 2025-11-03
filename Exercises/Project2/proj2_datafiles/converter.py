"""
File: converter.py
Project 7.5

Defines a class that converts infix expressions to postfix form.
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

    def __init__(self, scanner):
        self.scanner = scanner
        self.expressionSoFar = None

    def __str__(self):
        """Returns a string respentation of the postfix expression.
        Returns the portion of the expression that was converted so far.
        Also returns the operators still on the stack.
        """
        rv = "\n"
        if len(self.expressionSoFar) != 0:
            rv = "Expression so far:" + "".join(map(lambda esf: str(esf.getValue()) + " ", self.expressionSoFar)) + "\n"
        else:
            rv = "Expression so far: none\n" 

        if self.operatorStack.isEmpty():
            rv += "The stack is empty"
        else:
            rv += "Operators on stack: " + "".join(map(lambda os: str(os.getValue()) + " ", self.operatorStack))

        return rv

    # def conversionStatus(self):
        

    def convert(self):
        """Returns a list of tokens that represent the postfix
        form.  Assumes that the infix expression is syntactically correct
        
        Pseudocode:
        1) Start with Empty postfix expression and a stack
            * Stack will hold operators and left parentheses

        2) Scan across the infix expression

        3) On encountering operand
            * Append it to the post fix expression

        4) On encoutering left parenthesis
            * Push it onto the stack

        5) On encountering an operator
            * Pop off the stack all operators that have equal or higher precedence
            * Append them to the post fix expression
            * Push the scanned operator onto the stack

        6) On encountering right parenthesis
            * Shift operator from stack to postfix expression
              * Until meeting the matching left parenthesis which is discarded
        
        7) On encountering the end of infex
            * Transfer remaining operators from the stack to the postfix

        """
        # Step 1
        postfix = []
        self.expressionSoFar = postfix
        stack = ArrayStack()
        self.operatorStack = stack

        while self.scanner.hasNext(): # Step 2
            currentToken = self.scanner.next()
            if currentToken.getType() == Token.INT: # Step 3
                postfix.append(currentToken)
            elif currentToken.getType() == Token.LPAR: # Step 4
                stack.push(currentToken)
            elif currentToken.getType() == Token.RPAR: # Step 6
                topOperator = stack.pop()
                while topOperator.getType() != Token.LPAR:
                    postfix.append(topOperator)
                    topOperator = stack.pop()
            elif currentToken.isOperator(): # Step 5
                # TO DO: If the operatorStack is empty raise an AttributeError: Too few operators
                while (not stack.isEmpty()) \
                    and stack.peek().getPrecedence() >= currentToken.getPrecedence() and currentToken.getType() != Token.EXPO:
                    if stack.isEmpty():
                        raise AttributeError("Too few operators")
                    postfix.append(stack.pop())
                    

                stack.push(currentToken)
        
            elif currentToken.getType() == Token.UNKNOWN:
                raise AttributeError("Unrecognized symbol")
            


        while not stack.isEmpty():
            postfix.append(stack.pop())
        return postfix
   

def main():
    """A tester program for convert.py
    Performs the inputs and outputs. 
    """
    while True:
        s = input("Enter an infix expression:")
        if s =="":
            break
        scanner = Scanner(s)
        converter = IFToPFConverter(scanner)
        postfix = converter.convert()
        print("Postfix expression: ", "".join(map(lambda pf: str(pf.getValue()) + " ", postfix)))


if __name__ == "__main__":
    main()


