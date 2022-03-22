# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order.
long_string = "string containing multiple words"

def normal(i):
    forward = long_string
    return forward

def backwards(n):
    fun = ' '.join(n.split()[::-1])
    return fun

print(normal(long_string))
print(backwards(long_string))

