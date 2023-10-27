#!/usr/bin/python3

if __name__ == "__main__":

    from calculation import add, sub, mul, div
    a = 4 #use this variable as a first argument to call a function 
    b = 2 #use this variable as a second argument to call a function

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")

