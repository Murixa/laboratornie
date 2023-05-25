def p2():
    words = []
    while (new_words := str(input())) != "stop":
        words.append(new_words)
    print(" ".join(words))
p2()
def p3():

    words = []
    while (new_words := str(input())) !="stop":
        if "ф" in new_words or "Ф" in new_words:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
p3()
def pr4():
    from random import randint
    print("Для завершения игры нажмите: stop")
    while True:
        a = randint(1, 1000)
        b = randint(1, 1000)
        print(f"{a} + {b} = ", end = "" )
        res = input()
        while not res.isdigit() and res !="stop":
            print("Вы ввели что-то не то, введите снова", end = "")
            res = input()
        if res == "stop":
             break
        res == int(res)
        if a+b == res:
             print("Правильно!")
        else:
             print("Ответ неправильный!")
pr4()
