x = 0
while x < 10:
    x += 1
    if x == 5:
        print('x is 5')
        continue
    print(x)

# exercise
# use a while loop to create a list with only even values from 0 to 100
# do not add the value 58
even_number = []
x = 0
while x <= 100:
    if x % 2 == 0 and x != 58:
        even_number.append(x)
    x += 1

print(even_number)
