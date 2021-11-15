from random import randint

def fun(a, b):
    my_list = []
    my_dict = {}
    for i in range(10):
        x = randint(a, b)
        my_list.append(x)
        my_dict[i+1] = x
    return print(f'Список: {my_list},\nСловарь: {my_dict}')

fun(2, 100)