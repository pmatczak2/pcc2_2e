# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.

a_list = [1, 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10]


def no_duplicates():
    b_list = [x for x in a_list]
    return list(set(b_list))

print(no_duplicates())