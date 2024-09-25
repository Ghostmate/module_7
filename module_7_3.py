import codecs

trans_dict = {',': ' ',
              '.': ' ',
              '=': ' ',
              '!': ' ',
              '?': ' ',
              ';': ' ',
              ':': ' ',
              # ' - ': ' '
              }


class WordsFinder:
    def __init__(self,*args):
        self.file_names = args

    def line_words(self, string):
        table = str.maketrans(trans_dict)
        _s = string.translate(table)
        _s = _s.replace(' - ', ' ')
        return _s.split()

    def find(self, word):
        _w = word.lower()
        _dict = self.get_all_words()
        found_words = list()
        for f,v in _dict.items():
            if _w in v:
                found_words.append({f:v.index(_w) + 1})
        return found_words

    def count(self,word):
        _dict = self.get_all_words()
        found_count = 0
        for v in _dict.values():
            found_count += v.count(word.lower())
        return found_count


    def get_all_words(self, *args):
        exit_dict = dict()
        for f in self.file_names:
            _list = []
            with codecs.open(f, 'r', 'utf-8') as file:
                _string = file.readline()
                while _string != '':
                    _list.extend(self.line_words(_string.lower()))
                    _string = file.readline()
                exit_dict.update({f: _list})
        return exit_dict

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
