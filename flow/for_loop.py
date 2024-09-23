test_list = [1, 2, 3]
test_tuple = (1, 2, 3)
test_set = {1, 2, 3}
test_dict = {1: 'one', 2: 'two', 3: 'three'}
test_string = 'one two three'
test_num = 3

for x in test_string:
    print(x)

for x in range(test_num):
    print(x)

# exercise
practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 10, 4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if value is above 100

for list in practice_list:
    for num in list:
        if num < 50:
            if num < 10:
                continue
            print(num)
        elif num > 100:
            break
