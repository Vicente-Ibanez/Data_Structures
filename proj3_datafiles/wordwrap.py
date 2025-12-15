"""
File: wordwrap.py
Project 9.6

Copies words from one file to another, in such a manner that they
wrap within a given line width.  The line width and the input and
output file names are the inputs.  The line width should be no less
than 40 characters.
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def main():
    """ Main function to run the word wrap program. """
    # Take the input file name
    inName = input("Enter the input file name: ")
    # Take the output file name
    outName = input("Enter the output file name: ")
    # Take the line width
    lineWidth = int(input("Enter the line width: "))

    # Finish the program below:

    # Ensure the file line width is at least 40 characters
    if lineWidth < 40:
        print("The line width should be no less than 40 characters.")
        return

    # Read in the input file the user provides
    with open(inName, 'r') as file:
        # use a linked list because we will be adding to the end which is O(1) because getNode() tests for position len(self)-1
        # popping from the front which is O(1) because getNode() tests for position 1
        words = LinkedList() 
        for line in file:
            for word in line.split():
                words.add(word)

    # Write to the output file the user provides.
    with open(outName, 'w') as file:
        current_line = ""
        current_line_width = 0

        # While there are still words to process
        while len(words) > 0:
            # Get the next word 
            current_word = words.pop(0)

            # If the line does not have the capacity to fit the word and a space before the word,
            # write the current line to the file and start a new line with the current word
            if current_line_width + len(current_word) + 1 + (1 if len(words) > 0 else 0) > lineWidth:
                file.write(current_line + ("\n" if len(words) > 0 else ""))
                current_line = current_word
                current_line_width = len(current_word) 
            else:
                # The current line has space for the word (and a leading space if needed) 
                # This logic determines if a space is needed before the word, as the start of a line
                # does not need a leading space               
                current_line_width += len(current_word) + (1 if current_line != "" else 0)
                current_line += (" " if current_line != "" else "") + current_word 

                # If the current line is exactly the line width, write it to the file
                if current_line_width == lineWidth:
                    file.write(current_line + ("\n" if len(words) > 0 else ""))
                    current_line = ""
                    current_line_width = 0
                    
            
        # Write the remaining words in the current line to the file
        if current_line != "":
            file.write(current_line)


if __name__ == "__main__":
    main()


