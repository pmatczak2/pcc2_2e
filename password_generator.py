# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.
import random, string



letters = random.sample(string.hexdigits + string.punctuation, k= 16)
fun = "".join(letters)
print(fun)

def passsword(n):
    size = "".join(random.choice(string.hexdigits + string.punctuation) for _ in range(n))
    print(size)

passsword(16)