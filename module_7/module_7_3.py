import string


class WordsFinder:

    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file_now:
                    words = []
                    for line in file_now:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation + '—'))
                        words.extend(line.split())
                all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл{file_name} не найден')
        return all_words
    def find(self, word):
        for name, words in self.get_all_words().items():
            find_words = {}
            i = 1
            for j in words:
                if j.lower() == word.lower():
                    find_words[name] = i
                    return find_words
                    break
                i += 1

    def count(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            i = 0
            for j in words:
                if j.lower() == word.lower():
                    i += 1
            find_words[name] = i
        return find_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

