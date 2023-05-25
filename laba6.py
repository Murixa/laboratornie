def z1():
    countries={
        "russia" : "moscow",
        "brazil" : "brazilia",
        "france" : "paris",
        "finland" : "helsinki"
    }
    print('n1:')
    print("a",countries)
    x=input('Vvedite strany ')
    print("b", countries[x])
    print("c", sorted(countries))
z1()
def z2():
    och={
        1 : ['А','В','Е','И','Н','О','Р','С','Т'],
        2 : ['Д','К','Л','М','П','У'],
        3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        4 : ['Й', 'Ы'],
        5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        6 : ['Ш', 'Э', 'Ю'],
        7 : ['Ф', 'Щ', 'Ъ'],
    }
    print('n2:')
    x = input("Vvedite slovo")
    x=list(x)
    d=0
    for i in x:
        for k in och:
            if i in och[k]:
                d+=k
    print('vashe slovo stoit', d, 'ballov')
z2()
def z3():
    stu={
        'A' : ['eng','rus','spa'],
        'B': ['eng', 'rus', 'chi'],
        'C': ['eng', 'rus'],
        'D': ['rus', 'chi'],
        'E': ['rus'],
        'F': ['eng', 'spa'],
        'G': ['kz', 'rus'],
        'H': ['eng', 'it'],
        'I': ['eng', 'fr'],
    }
    d = []
    c = 0
    k=[]
    for i in stu:
        for i in stu[i]:
            if i not in d:
                d.append(i)
                c+=1
    for i in stu:
        if 'chi' in stu[i]:
            k.append(i)
        else:
            continue
    print('n3:')
    print(*d)
    print('vsego yazikov:',c)
    print(*(sorted(d)))
    print('znaut kitayski', *k)
z3()