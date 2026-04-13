print("~~~ ЗАМЕНА СЛОВ В ТЕКСТЕ ~~~")

text = input("Введите текст: ")

old_word = input("Какое слово заменить: ")
new_word = input("На что заменить: ")

if old_word in text:
    result = text.replace(old_word, new_word)
    print()
    print("Готово!) Вот результат:")
    print(result)
else:
    print()
    print("Такого слова в тексте нет.")