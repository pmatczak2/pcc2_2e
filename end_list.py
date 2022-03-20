# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
# first and last elements of the given list. For practice, write this code inside a function.

a_list = [5, 10, 15, 20, 25]

ans = a[::len(a)-1]
print(ans)



first_last = [a_list[n] for n in (0, -1)]
print(first_last)



def list_ends(a_list):
    return [a_list[0], a_list[len(a_list) - 1]]

print(list_ends(a_list))
