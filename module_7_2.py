def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    string_positions = {}
    line = 1
    for string in strings:
        string_positions[(line, file.tell())] = string
        file.write(string)
        file.write('\n')
        line += 1
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)