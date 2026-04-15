print("~~~ ЗАМЕНА СЛОВ В СТРОКЕ ~~~")

text = input("Введите текст: ")

if text.strip() == "":
    print("Ошибка: строка пустая. Попробуйте снова.")
else:
    old_word = input("Какое слово заменить: ")
    new_word = input("На что заменить: ")

    if old_word.lower() in text.lower():
        words = text.split()
        result_words = []

        for word in words:
            if word.lower() == old_word.lower():
                result_words.append(new_word)
            else:
                result_words.append(word)

        result = " ".join(result_words)

        print()
        print("Готово! Вот результат:")
        print(result)
    else:
        print()
        print("Такого слова в строке нет.")
