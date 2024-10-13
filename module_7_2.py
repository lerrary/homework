def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'a', encoding="utf=8")

    for i in strings:
        string_positions.update({(strings.index(i)+1,file.tell()): str(i)})
        file.write(f'{str(i)}\n')
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
