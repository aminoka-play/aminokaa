print("~~~ ЗАМЕНА СЛОВ В СТРОКЕ ~~~")

while True:
    print()
    text = input("Введите текст: ")

    if text.strip() == "":
        print("Ошибка: строка пустая.")
        continue

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

    print()
    while True:
        again = input("Хотите выполнить ещё одну замену? (да/нет): ")

        if again.lower() == "да":
            break

        elif again.lower() == "нет":
            print("Программа завершена.")
            exit()  
        else:
            print("Пожалуйста, введите только 'да' или 'нет'.")
