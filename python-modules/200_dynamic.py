#!/usr/bin/python3

import sys

def main():
    # Get the command-line arguments
    arguments = sys.argv[1:] # Start from index 1 because in sys.args the 0 index is used for file name!
    num_arguments = len(arguments)

    # Print the number of arguments and appropriate message
    if num_arguments == 0:
        print("0 arguments.")
    else:
        if num_arguments == 1:
            print(f"1 argument:")
        else:
            print(f"{num_arguments} arguments:")

        # Printing each of the user-provided command-line arguments along with their position.
        position = 1
        for arg in arguments:
            print(f"{position}: {arg}")
            position += 1

# Code should not be executed when imported
if __name__ == "__main__":
    main()
