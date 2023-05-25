from PIL import Image
import os
import csv
def z1():
    os.mkdir('/Users/user/Downloads/dd')
    k = 0
    for i in os.listdir('/Users/user/Downloads/jj'):
        img = Image.open(i)
        img = img.resize((img.width // 3, img.height // 3))
        k += 1
        img.save("/Users/user/Downloads/dd,img" + i + ".jpg")
z1()
def z2():
    k=1
    import os
    os.mkdir('/Users/user/Downloads/ddd')
    for i in os.listdir('labora9'):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = Image.open(i)
            img = img.resize((img.width // 3, img.height // 3))
            img.save("hhdhhjhjh" + str(k) + ".jpg")
            k+=1
z2()
def z3():
    itogo=0
    print('Nugno kupit:')
    with open('data.cvs.') as file:
        file = csv.reader(file)
        for i in file:
            name=i[0]
            k=int(i[1])
            cn=int(i[2])
            itogo+=k*cn
            print(name,' ',k, 'sht.cza',cn,'rub')
    print("summa: ", itogo)
z3()


