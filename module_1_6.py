my_dict = {"Маша": 2000, "Паша": 2001, "Сережа": 2005}
print('Dict', my_dict)
print('Existing value', my_dict.get("Маша"))
print('Not existing value', my_dict.get("Коля"))
my_dict.update({"Дима": 2004, "Аня": 2007})
print('Deleted value', my_dict.pop("Паша"))
print('Modified Dict', my_dict)

my_set = {1, 2.14, "Метро", 2.14, (2, 3, 5)}
print('Set:',my_set)
my_set.add('Рыцарь')
my_set.discard(1)
print('Modified Set:', my_set)



