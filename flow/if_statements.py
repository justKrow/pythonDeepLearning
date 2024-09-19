# run code if value is greater than 10

x = 0

if x > 10:
    print("x is greater than 10")
    print("another line")
    y = 10
    print(y)
elif x != 0:
    print("elif statement is true")
else:
    print("code running cuz if statemetn is false")

if 1 in [1, 2, 3]:
    print("1 is in the list")

print("i am outside of if statement")

# exercise
money_available = 50

if money_available >= 80:
    print("eat sth fancy")
elif money_available > 45:
    print("eat sth nice")
elif money_available > 15:
    print("eat sth okay")
else:
    print("eat sth cheap")
