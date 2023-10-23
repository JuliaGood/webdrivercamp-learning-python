#!/usr/bin/env python3

def is_case(c): 
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False

print(f'B is {"lower" if is_case("B") else "upper"}')
print(f'a is {"lower" if is_case("a") else "upper"}')
print(f'F is {"lower" if is_case("F") else "upper"}')
print(f'f is {"lower" if is_case("f") else "upper"}')
print(f'I is {"lower" if is_case("I") else "upper"}')

