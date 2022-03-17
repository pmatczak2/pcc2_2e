# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
# number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this
# opportunity to practice using functions, described below.
num = int(input('Is the number prime or not: '))

for i in range(2, num):
    if num % i == 0:
        print('not prime')
        break
else:
    print('prime')