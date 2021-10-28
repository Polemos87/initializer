import json
import hashlib


class MyIterator:

    def __iter__(self):
        self.countries = self.get_file()
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        country = self.countries.pop()
        self.name = country['name']['common']
        self.name_link = self.name + (' - https://en.wikipedia.org/wiki/'+ self.name.replace(' ', '_'))
        with open ('new_file.txt', 'a', encoding="utf-8") as file:
            file.write(self.name_link + '\n')

        return self.name_link

    def get_file(self):
        with open('countries.json') as file:
            self.source_file = json.load(file)
            return self.source_file
#
for name in MyIterator():
    pass


def general(path):
    with open(path, encoding='utf-8') as my_file:
        for i in my_file:
            hash_object = hashlib.md5(i.encode())
            yield hash_object.hexdigest()


for i in general('new_file.txt'):
    print(i)