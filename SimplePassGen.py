import random

lower = 'abcdefghijklmnopqrstuvwzyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'
number = '0123456789'
symbol = '[]{}#()*;._-'

all = lower + upper + number + symbol
length = 16
password = ''.join(random.sample(all, length))
print(f'Password: {password}')