from array_stack import ArrayStack
from linked_stack import LinkedStack

def test(stack_type):
    # Test any implementation with teh same code
    s = stack_type()
    print("Length:", len(s))
    print("Is empty:", s.is_empty())
    print("Push 1-10")
    
    for i in range(10):
        s.push(i+1)

    print("Peeking:", s.peek())
    print("Items (bottom to top):", s)
    print("Length:", len(s))
    print("Empty", s.is_empty())

    the_clone = stack_type(s)

    print("Items in clone (bottom to top):", the_clone)
    the_clone.clear()
    print("Length of clone after clear:", len(the_clone))
    print("Push 11")
    s.push(11)
    print("Popping items (top to bottom):", end=" ")
    while not s.is_empty(): print(s.pop(), end=" ")
    print("\nLength after pops:", len(s))
    print("Empty:", s.is_empty())

# test(ArrayStack)
test(LinkedStack)