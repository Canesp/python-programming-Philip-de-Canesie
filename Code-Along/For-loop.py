for i in range(5):
    print(i, "hej")

for i in range(10):
    print(i, end= " ")

mysum = 0

for i in range(10):
    mysum += i

print(f"{mysum=}") 

cute_animals = ["rabbit", "pig", "cat", "dog"]

for animal in cute_animals:
    print(f"{animal}" + " is cute")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numbers:
    print(f"{x}")
    #n -= 1


import random as rnd

number_sixes = 0
number_rolls = 10

for i in range(number_rolls):
    dice = rnd.randint(1, 6)
    if dice == 6:
        number_sixes += 1

print(f"{number_sixes=}")
print(f"{number_sixes / number_rolls}")

#uppgift 1:

import math as math

for t in range(10000):
    p = .791 * math.exp(.0526 * t)
    if p >= 15:
        print(f"år {1960 + t} är konsumptionen 15kg/person per år")
        break


#import matplotlib as plt

pasta_per_year = []

for t in range(140):
    pasta_con = .791 * math.exp(.0526 * t)
    pasta_per_year.append(pasta_con)

#plt.plot(range(1960, 2100), pasta_per_year)
