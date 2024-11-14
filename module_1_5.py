immutable_var = 1, 2, 'City', False
print('это кортеж, отображен в круглых скобках:', immutable_var)
# immutable_var[0] = 13 -- невозможно изменить элемент кортежа ошибка:
# "TypeError: 'tuple' object does not support item assignment"
mutable_list = [1, 2, 'City', False]
print('это список, отображен в квадратных скобках: ', mutable_list)
mutable_list[0] = 13
mutable_list.append('Modified')
print('измененный список: ', mutable_list)


