"""
File: wordwrap.py
Project 9.6

Copies words from one file to another, in such a manner that they
wrap within a given line width.  The line width and the input and
output file names are the inputs.  The line width should be no less
than 40 characters.

Programmer: Vicente Ibanez
Problem: Enforcing line widths for text files.
Date: 12/15/2025
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def process_file(inName, outName, lineWidth):
    """ Process File Function 
    General outline: 
    User specifies the input and output file names and the line width.
    The program reads the file into a list of sublists and ensure that the length 
    of the line is <= user’s line length.
    Then the program writes the contents to the output file.
    """
    # Ensure the file line width is at least 40 characters
    if lineWidth < 40:
        raise ValueError("The line width should be no less than 40 characters.")

    # Read in the input file the user provides
    with open(inName, 'r') as file:
        # use arraylist of arraylist because linkedlist has additional overhead for each item
        # and we don't need to do insert/delete in the middle of the list (which linkedlist does in faster time)
        all_lines = ArrayList() 
        current_line = ArrayList()
        current_line_width = 0
        
        for line in file:

            for current_word in line.split():

                # If the line does not have the capacity to fit the word and a space before the word,
                # write the current line to the file and start a new line with the current word
                if current_line_width + len(current_word) + 1 + (1 if len(all_lines) > 0 else 0) > lineWidth:
                    all_lines.append(current_line)
                    current_line = ArrayList()
                    current_line.append(current_word)
                    current_line_width = len(current_word) 
                else:
                    # The current line has space for the word (and a leading space if needed) 
                    # This logic determines if a space is needed before the word, as the start of a line
                    # does not need a leading space               
                    current_line_width += len(current_word) + (1 if len(current_line) != 0 else 0)
                    current_line.append((" " if len(current_line) != 0 else "") + current_word)

                    # If the current line is exactly the line width, write it to the file
                    if current_line_width == lineWidth:
                        all_lines.append(current_line + ("\n" if len(all_lines) > 0 else ""))
                        current_line = ArrayList()
                        current_line_width = 0
                        
            
        # Write the remaining words in the current line to the file
        if current_line != "":
            # file.write(current_line)
            all_lines.append(current_line)
    
    # Write all lines to the output file
    with open(outName, 'w') as file:
        for line in all_lines:
            file.write("".join(line) + ("\n" if line != all_lines[len(all_lines)-1] else ""))

def main():
    """ Main function to run the word wrap program. 
    General outline: 
    User specifies the input and output file names and the line width.
    The program reads the file into a list of sublists and ensure that the length 
    of the line is <= user’s line length.
    Then the program writes the contents to the output file.
    """

    # Take the input file name
    inName = input("Enter the input file name: ")
    # Take the output file name
    outName = input("Enter the output file name: ")
    # Take the line width
    lineWidth = int(input("Enter the line width: "))

    # Finish the program below:
    process_file(inName, outName, lineWidth)
    
def testMain():
    """ Test function to run the program and check its output."""
    input = 'proj3.txt'
    output = 'output.txt'
    try:
        process_file(input, output, 39)
        print("Test 1 failed: Value Error Exception  not raised for line width < 40.")
    except ValueError as e:
        print("Test 1 passed: Caught Value Error exception as expected for line width < 40.")
    else:
        print("Test 1 failed: Value Error Exception not raised for line width < 40.", e)
    
    try:
        process_file(input, output, 50)
        with open("output.txt", 'r') as file:
            content = file.read()

            if any(len(line) > 50 for line in content.splitlines()):
                print("Test 2 failed: Line exceeds specified width of 50 characters.")
                                
            else:
                print("Test 2 passed: File processed successfully with line width 50.")
    except Exception as e:
        print("Test 2 failed: Unexpected exception raised:", e)

    except Exception as e:
        print("Test 2 failed: Unexpected exception raised:", e)


if __name__ == "__main__":
    main()
    # testMain()


