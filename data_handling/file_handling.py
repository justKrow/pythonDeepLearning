# file = open('test.txt')
# print(list(file))
# file.close()

# open and close automatically
with open('test.txt') as file:
    print(file.read())

# write some file
with open('test.txt', 'a') as file:
    file.write('Hello, World!\n')
    file.write('This is a test.\n')
