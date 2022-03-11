prompt = input("Is the string palindrome?: ")

def is_palindrome(prompt):
    return prompt == prompt[::-1]

answer = is_palindrome(prompt.upper())
if answer:
    print('Yes')
else:
    print("no")
