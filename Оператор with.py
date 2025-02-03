import re
class WordsFinder():
    file_names = []
    all_words = {}
    def __init__(self,*args):
        for i in args:
            with open(i, 'r', encoding='utf-8') as file:
                text_mas = []
                text = file.read()
                text = re.split(r"[,;:»«?=!\s\n]", text)
                for j in text:
                    if j.lower() not in text_mas:
                            text_mas.append(j.lower())
                self.all_words.update({i: text_mas})
            self.file_names.append(i)

    def creation_of_glos(self):
        for i in self.file_names:

            with open(i, 'r', encoding='utf-8') as file:
                text_mas = []
                text = file.read()
                text = re.split(r"[,;:»«?=!\s\n]", text)
                for j in text:
                    if j.lower() not in text_mas:
                        text_mas.append(j.lower())
                self.all_words.update({i: text_mas})

    def get_all_words(self):
        print(self.all_words)

    def find(self,word):
        for name, words in self.all_words.items():
            counter=0
            for i in words:
                if word.lower()==i:
                    counter+=1
                    print(f'Название файла: {name}, Порядковый номер: {counter}')

    def counter(self,word):
        for name, words in self.all_words.items():
            counter=0
            with open(name, 'r', encoding='utf-8') as file:
                text_mas = []
                text = file.read()
                text = re.split(r"[,;:»«?=!\s\n]", text)
                for j in text:
                    if word.lower() == j.lower():
                        counter += 1
                print(f'Название файла: {name}, Колличество слов: {counter}')





finder2 = WordsFinder('test_file.txt')
finder2.get_all_words() 
finder2.find('Не')
finder2.counter('Не')