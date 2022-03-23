# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.
import random, string

letters = random.sample(string.hexdigits + string.punctuation, k=16)
for letter in letters:
         print(letter, end="")



def password(length):
    letter = string.hexdigits + string.punctuation
    letter_result = ''.join(random.choice(letter) for i in range(length))
    print(letter_result)

password(10)