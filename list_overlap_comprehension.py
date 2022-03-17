# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python
# using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
import random

random_list = [i for i in range(1, 15)]

for i in range(1, 15):
	n = random.randint(1, 30)
	random_list.append(n)


random_list2 = []
for j in range(1, 10):
	x = random.randint(1, 30)
	random_list2.append(x)





c = list(set([i for i in random_list if i in random_list2]))
print(c)
# # c = []
# for i in a:
# 	if i in b and i not in c:
# 		c.append(i)



