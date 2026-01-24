from linkedstack import LinkedStack

def brackets_balance(exp):
    """ exp is a string that represents the expression 
    """
    stk = LinkedStack()
    for ch in exp: # Scan across the expression
        if ch in ["[", "("]: # Push an opening bracket
            stk.push(ch)
        
        elif ch in ["]", ")"]: # Process closing bracket
            if stk.is_empty(): # not balanced
                return False
            
            ch_from_stack = stk.pop()
            # Brackets must be of the same type and match up
            if ch == "]" and ch_from_stack != "[" or \
            ch == ")" and ch_from_stack != "(":
                return False
        
    return stk.is_empty() # Balanced if stack is empty at the end
    
def main():
    exp = input("Enter a bracket expression: ")
    if brackets_balance(exp):
        print("The expression is balanced")
    else:
        print("The expression is not balanced")

if __name__ == "__main__":
    main()