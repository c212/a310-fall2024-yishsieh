#hw2

#Q1 craps


import random

wins = 0
howMany = 1000000

for times in range(howMany):
  d1 = random.randrange(1, 7)
  d2 = random.randrange(1, 7)
  sum_d = d1 + d2
  if sum_d == 7:
    wins += 4
  else:
    wins -= 1
print("Question 1: ", wins/howMany)


#====================

#Q2 three dice, prime number
#possibilities of not prime number

# all = 6*6*6 = 216
# 3~18
# prime numbers = [3, 5, 7, 11, 13, 17] -6

# sum = 3, [1, 1, 1]
# sum = 5, [1, 2, 2], [1, 1, 3]...
# ...
# sum = 17, [...]

# total --> 73 ways

# 1 - (73/216) =~ 0.66
import numpy as np
prime_numbers = [3, 5, 7, 11, 13, 17]
exp = 10000
not_prime_counter = 0

for i in range(exp):
  # randomely select 3 numbers from 3 dice
  game = np.random.choice([1,2,3,4,5,6], 3)
  # sum up all 
  game_sum = sum(game)
  # if-condition: if the sum is not prime numbers, counter + 1
  if game_sum not in prime_numbers:
    not_prime_counter +=1 


# print the possiblities 
print(not_prime_counter / exp)


#=======================

#Q3 Locker problem


#=======================

#Q4 Flip coin


#=====================

#Q5 Complex function


#========================
#Q6 Creature 