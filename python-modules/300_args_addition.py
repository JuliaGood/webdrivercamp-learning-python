#!/usr/bin/python3

import sys

def main():
    # Get the command-line arguments as integers and calculate the sum
    arguments = sys.argv[1:] # Start from index 1 because in sys.args the 0 index is used for a script name
   
    result = 0

    for arg in arguments:
        result += int(arg) # Cast arguments into integers

    print(result)

# Code should not be executed when imported
if __name__ == "__main__":
    main()
