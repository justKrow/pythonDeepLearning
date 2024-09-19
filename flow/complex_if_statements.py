if True and True and False or True:
    print(True)

# exercise
money_available = 100
hungry = True
bored = True
# check if money_available > 80 and if hungry is True or bored is True

if money_available > 80 and hungry == True or bored == True:
    print("eat sth fancy")

# nested if statements
x = '1'
if x in ['a', 'b', '1']:
    print("a is in the list")
    if x.isalpha():
        print("a is an alphabet")
    if True:
        print("something")

# exercise
money_available = 100
hungry = False
bored = True
# create a nest if statement that runs of all 3 conditions are true (money > 80 for the first one)

if money_available > 80:
    print("i am rich")
    if hungry:
        print("i am hungry")
        if bored:
            print("lets eat sth fancy")
