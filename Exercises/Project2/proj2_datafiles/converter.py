"""
File: converter.py
Project 7.5

Defines a class that converts infix expressions to postfix form.

Programmer: Vicente Ibanez
Problem: Converting a infix statement to a postfix statement that a user inputs.
Date: 11/03/2025
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

    def __init__(self, scanner):
        self.scanner = scanner
        self.expressionSoFar = None
        self.current_token = None

    def __str__(self):
        """Returns a string respresentation of the postfix expression.
        Returns the portion of the expression that was converted so far.
        Also returns the operators still on the stack.
        """
        rv = "\n"
        if len(self.expressionSoFar) != 0:
            rv = "Portion of expression processed: " + "".join(map(lambda esf: str(esf.getValue()) + " ", self.expressionSoFar)) + "\n"
        else:
            rv = "Portion of expression processed: none\n" 

        if self.operatorStack.isEmpty():
            rv += "The stack is empty"
        else:
            rv += "Operators on stack: " + "".join(map(lambda os: str(os.getValue()) + " ", self.operatorStack))

        return rv

    def conversionStatus(self):
        """This method is used to display the current state of the conversion.
        It returns the portion of the expression scanned. 
        It can be used to assist with error handling."""
        rv = "\n"
        if len(self.expressionSoFar) != 0:
            rv = "Portion of expression processed: " + "".join(map(lambda esf: str(esf.getValue()) + " ", self.expressionSoFar)) + "\n"
        else:
            rv = "Portion of expression processed: none\n" 

        if self.operatorStack.isEmpty():
            rv += "The stack is empty"
        else:
            rv += "Operators on stack: " + str([x.getValue() for x in self.operatorStack])

        return rv


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

        numOperators = 0
        numOperands = 0

        while self.scanner.hasNext(): # Step 2
            currentToken = self.scanner.next()
            self.current_token = currentToken

            if currentToken.getType() == Token.UNKNOWN:
                raise AttributeError("Unrecognized symbol")
            elif currentToken.getType() == Token.INT: # Step 3
                postfix.append(currentToken)
                numOperands += 1
            elif currentToken.getType() == Token.LPAR: # Step 4
                stack.push(currentToken)
            elif currentToken.getType() == Token.RPAR: # Step 6
                if stack.isEmpty():
                    raise AttributeError("Too few operators")
                topOperator = stack.pop()
                while topOperator.getType() != Token.LPAR:
                    postfix.append(topOperator)
                    if stack.isEmpty():
                        # no left parenthesis
                        raise AttributeError("Too few operators")
                    topOperator = stack.pop()
            elif currentToken.isOperator(): # Step 5
                numOperators += 1
                if len(postfix) == 0:
                    raise AttributeError("Too few operators")
                while (not stack.isEmpty()) \
                    and stack.peek().getPrecedence() >= currentToken.getPrecedence() \
                    and currentToken.getType() != Token.EXPO:
                    postfix.append(stack.pop())

                stack.push(currentToken)
            
        while not stack.isEmpty():
            postfix.append(stack.pop())

        if numOperands - numOperators != 1:
            raise AttributeError("Too few operators")
        
        return postfix
   

def main():
    """A tester program for convert.py
    Performs the inputs and outputs. 
    """
    while True:
        s = input("Enter an infix expression:")
        if s =="":
            break

        try:
            scanner = Scanner(s)
            converter = IFToPFConverter(scanner)
            postfix = converter.convert()
            print("Postfix expression: ", "".join(map(lambda pf: str(pf.getValue()) + " ", postfix)))
        except Exception as e:
            print(e)
            print(converter.conversionStatus())
            # print("The token that caused the error:", str(converter.current_token.getValue()))


def testMain(testCase):
    """This function acts line the main function for the test() function."""
    try:
        scanner = Scanner(testCase)
        converter = IFToPFConverter(scanner)
        postfix = converter.convert()
        print("Postfix expression: ", "".join(map(lambda pf: str(pf.getValue()) + " ", postfix)))
    except Exception as e:
        print(e)
        print(converter.conversionStatus())
        raise e

def test():
    """ A tester function for convert.py"""
    test1 = "3 * 0"
    test2 = "3 4 2 5"
    test3 = "5 + 6 - 3 & 9"
    test4 = "2 $ 3"
    test5 = "2$"
    try:
        testMain(test1)
        print("Test 1 Passed")
    except Exception as e:
        print("Test 1 Failed", e)

    try:
        testMain(test2)
        print("Test 2 Failed")
    except Exception as e:
        print("Test 2 Passed", e)

    try:
        testMain(test3)
        print("Test 3 Failed")
    except Exception as e:
        print("Test 3 Passed", e)

    try:
        testMain(test4)
        print("Test 4 Failed")
    except Exception as e:
        print("Test 4 Passed", e)
    
    try:
        testMain(test5)
        print("Test 5 Failed")
    except Exception as e:
        print("Test 5 Passed", e)

    print("The test above made sure postfix was working as expected and tested every exception.")


if __name__ == "__main__":
    main()
    # test()


