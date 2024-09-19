from pathlib import Path
import codecs

def custom_write(file_name, strings):
    Path(file_name).touch()
    string_positions = dict()
    file = codecs.open(file_name,'w',"utf-8")
    i = 0
    for s in strings:
        a = file.tell()
        b = s
        file.write(s + '\n')
        string_positions.update({(i,a):b})
        i += 1
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