def load():
    dictionary = {}

    with open('dictionary.txt', 'r', encoding='utf-8') as file:
        for line in file:
            english, ukrainian = line.strip().split(',')
            dictionary[english] = ukrainian       
    return dictionary

dictionary = load()
word = input("Введіть англійське слово: ")
print("Переклад:", dictionary.get(word, "Переклад не знайдено"))
