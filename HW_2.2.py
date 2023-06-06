dictionary = {}

def add_word(word, translation):
    dictionary[word] = translation
    print("Слово успешно добавлено в словарь.")

def delete_word(word):
    if word in dictionary:
        del dictionary[word]
        print("Слово успешно удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def search_word(word):
    if word in dictionary:
        translation = dictionary[word]
        print(f"{word}: {translation}")
    else:
        print("Слово не найдено в словаре.")

def replace_word(word, translation):
    if word in dictionary:
        dictionary[word] = translation
        print("Перевод слова успешно заменен.")
    else:
        print("Слово не найдено в словаре.")


add_word("apple", "pomme")
add_word("banana", "banane")
search_word("apple")
replace_word("apple", "la pomme")
delete_word("banana")
search_word("banana")
input("press any key to close window")
