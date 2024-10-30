print(eval('5+10'))
print(eval('"test".upper()'))
# eval('if True: print("Hello")')
exec('if True: print("Hello")')

my_string = 'test'
method_list = ['upper', 'title', 'lower', 'casefold']
for method in method_list:
    print(eval(f'my_string.{method}()'))
