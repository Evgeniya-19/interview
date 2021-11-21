"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def fun(keys, values):
    my_dict = {}
    if len(keys) <= len(values):
        values1 = values[:len(keys)]
        x = {x: y for x, y in zip(keys, values1)}
    elif len(keys) > len(values):
        keys1 = keys[:len(values)]
        keys2 = keys[len(values):]
        x = {x: y for x, y in zip(keys1, values)}
        x_1 = my_dict.fromkeys(keys2,None)
        new_dict = x.update(x_1)
    return x


keys = ['a', 'b', 'c', 'd']
values = [1, 2]
values_1 = [1, 2, 3, 4, 5]
print(fun(keys, values))
print(fun(keys, values_1))
