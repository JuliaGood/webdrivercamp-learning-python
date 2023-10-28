#!/usr/bin/python3

num_list = [5, 4, 3, 2, 1]

# using a while loop
# it does not modify the original list. 
# it iterates through a list in reverse order and print its elements.
def print_list_1(list_):
    num = len(list_) - 1
    while num >= 0:
        print(list_[num])
        num -= 1

# using list slicing 
# it does not modify the original list. 
# It creates a new list with the elements in reverse order.
def print_list_2(list_):
    for num in list_[::-1]:
        print(num)

# using build-in "reversed" function
# it does not modify the original list. 
# it returns a separate iterator or list.
# we have to convert the reverse iterator to a list using list()
def print_list_3(list_):
    for num in list(reversed(list_)):
        print(num)

# using build-in ".reverse()" method
# it modifies the original list and does not return a new list
def print_list_4(list_):
    list_.reverse()
    for num in list_:
        print(num)

print('reversed list using 1st way: ')
print_list_1(num_list)
print('original list: ', num_list)

print('reversed list using 2nd way: ')
print_list_2(num_list)
print('original list: ', num_list)

print('reversed list using 3rd way: ')
print_list_3(num_list)
print('original list: ', num_list)

print('reversed list using 4th way: ')
print_list_4(num_list)
print('original list: ', num_list)
