"""
Домашнее задание по теме "Оператор "with"
"""


class WordsFinder:
    file_names = []

    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                list_words = []
                replased = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    new_line = line.lower()
                    for i in replased:
                        new_line = new_line.replace(i, '')
                    list_words += new_line.split()
            all_words[file_name] = list_words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        result = {}
        for file_name, words in all_words.items():
           for i, w in enumerate(words):
                if w == word:
                    result[file_name] = i + 1
                    break
        return result

    def count(self, word):
        all_words = self.get_all_words()
        search_word = word.lower()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(search_word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())                            # Все слова
print(finder2.find('TEXT'))                               # 3 слово по счёту
print(finder2.count('teXT'))                              # 4 слова teXT в тексте всего
