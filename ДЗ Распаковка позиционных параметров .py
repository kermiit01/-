def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

values_dict=[52,'Пятьдесят два',True]
values_list={'a':False,'b':[1,2,3],'c':'Пример'}
values_list_2 = [54.32, 'Строка' ]

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_dict)
print_params(**values_list)
print_params(*values_list_2, 42)