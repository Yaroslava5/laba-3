def p2():
    words = []
    while (new_word := str(input())) != "stop":
        words.append(new_word)
    print(" ".join(words))


def p3():
    words = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")


def p4():
    from random import randint
    print("Для завершения игры нажмите: stop")
    x = 0
    s = 0
    while True:
        a = randint(1, 1000)
        b = randint(1, 1000)
        print(f"{a} + {b} = ", end = "" )
        res = input()
        while not res.isdigit() and res != "stop":
            print("Вы ввели что-то не то, введите снова", end = "")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            x += 1
            print("Правильно!")
        else:
            print("Ответ неправильный!")
            s += 1
        if s == 3:
            print("Игра окончена. Правильных ответов:", s)


p2()
p3()
p4()
