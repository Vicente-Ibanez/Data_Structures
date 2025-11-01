from Data_Strucutures.stacks import Stacks

def parentheses_matching(s: str):
    stack = Stacks()
    for sub_s in s:
        if sub_s == "(":
            stack.push(sub_s)
        elif not stack.is_empty():
            stack.pop()
        else:
            return False
    return stack.is_empty()


def multiparentheses_matching(s:str):
    stack = Stacks()
    for sub_s in s:
        if sub_s in "([{":
            stack.push(sub_s)
        elif not stack.is_empty() and symbol_match(sub_s, stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()

def symbol_match(symbol:str, peek):
    symbol_match = {"(":")", "[":"]", "{":"}"}
    return symbol == symbol_match[peek]
    


# print("Test Case 1: ", parentheses_matching("((()))")==True)
# print("Test Case 2: ", parentheses_matching("()()))")==False)
# print("Test Case 3: ", parentheses_matching("(()))")==False)
# print("Test Case 4: ", parentheses_matching(")")==False)
# print("Test Case 4: ", parentheses_matching("(")==False)

print("Test Case 1: ", multiparentheses_matching("((()))")==True)
print("Test Case 2: ", multiparentheses_matching("{{{}}}")==True)
print("Test Case 3: ", multiparentheses_matching("[[[]]]")==True)
print("Test Case 4: ", multiparentheses_matching("{[()]}")==True)
print("Test Case 5: ", multiparentheses_matching("({)}")==False)