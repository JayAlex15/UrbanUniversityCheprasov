class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_str = file.read().lower()
                file_chars = []
                file_new_str = ''
                for char in file_str:
                    if char in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        file_chars.append(' ')
                    else:
                        file_chars.append(char)
                file_new_str = "".join(file_chars)
                all_words[file_name] = file_new_str.split()
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            index_count = 0
            for i in range(len(words)):
                index_count += 1
                if word.lower() == words[i]:
                    result[name] = index_count
                    break
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    counter += 1
                    result[name] = counter

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
