def z1():
    print("n1")
    l = [65, 2566, 329, 8, 33]
    x =int(input('vvedite chislo '))
    if x in l:
        print('vi ugadali')
        print(l)
    else:
        print('net,vi ne ugadali')
        print(l)
z1()
def z2():
    d = []
    s = [7, 1, 0, 1, 0, 75, 62, 88]
    for x in s:
        if s.count(x) > 1:
            d.append(x)
    print("n2")
    print(*d)
z2()
def z3():
    print("n3")
    week = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
    x = int(input('ВВедите кол-во выходных '))
    for i in week:
        print('рабочие:', *week[:-x])
        print('Выходные:', *week[-x:])
        break
z3()
def z4():
    print("n4")
    import random
    g1=('Иванов','Филипенко','Юниверс','Разумовский','Волков')
    g2 = ('Гром', 'Пчелкина', 'Дубин', 'Дагбаев', 'Макарова')
    x1=[]
    x2=[]
    x=[]
    x1.append(random.sample(g1,5))
    x2.append(random.sample(g2,5))
    x.extend(*x1)
    x.extend(*x2)
    x=tuple(x)
    print('a', x)
    print('b',g1)
    print('b', g2)
    print('b', x)
    print('c', len(x))
    print('d', *sorted(x))
    print('e', 'Иванов' in x)
    print('e', x.count('Иванов'))
z4()