class WordsFinder:
    file_names = []
    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            word_i = []
            with open(str(i), 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for j in line.split():
                        _ex = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
                        for h in _ex:
                            j = j.replace(h, '')
                        word_i.append(j)
            all_words.update({(i): word_i})
        return (all_words)

    def find(self, word):
        find_w = {}
        for i in range(0, len(list(self.get_all_words().values()))):
            find_list = list(self.get_all_words().values())[i]
            num = 1
            for j in find_list:
                if word.lower() == j:
                    find_w.update({self.file_names[i]: num})
                    break
                else:
                    num += 1
        return find_w
    def count(self, word):
        count_w = {}
        for i in range(0, len(list(self.get_all_words().values()))):
            count_list = list(self.get_all_words().values())[i]
            num = 0
            for j in count_list:

                if word.lower() == j:
                    num += 1
            count_w.update({self.file_names[i]: num})
        return count_w


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
