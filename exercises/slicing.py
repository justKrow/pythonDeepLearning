test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(test_list[0:8:2])

negative_slicings = test_list[-1:4:-1]
print(negative_slicings)

default_slicings = test_list[::2]
print(default_slicings)

# exercise
# start from 8 and go to 2, pick every second element
exercise_slicings = test_list[7:0:-2]
print(exercise_slicings)
