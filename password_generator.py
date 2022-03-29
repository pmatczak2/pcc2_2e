# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.
import random, string

password_length = random.randint(8, 16)

letters = random.sample(string.hexdigits + string.punctuation, password_length)
fun = "".join(letters)


print(len(fun))

# def passsword(n):
#     size = "".join(random.choice(string.hexdigits + string.punctuation) for _ in range(n))
#     print(size)
#
# passsword(16)