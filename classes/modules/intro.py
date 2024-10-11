import random
from math import floor as f
import string
from datetime import datetime

random_number = random.randint(0, 10)
print(random_number)

test_list = ['apple', 'orange', 'grapes']
print(random.choice(test_list))

print(string.ascii_lowercase)

print(f(4.7))

print(datetime.now())
