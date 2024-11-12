import random
import pandas as pd

a = 0

list1 = []

while a < 1000:
    random_number = random.randint(1, 6)
    if random_number == 1:
        list1.append(random_number)
    a += 1

print('횟수:', len(list1))
print('비율', len(list1) / 1000)