def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params()
print_params(10, False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Hello', 53, True]
values_dict = {'a': 3, 'b': False, 'c': 'yes'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [52, 'tip']
print_params(*values_list_2, 42)
