import json
def z1():
    products = {"products":
        [
            {
                "name": "Shokolad",
                "price": 100,
                "available": True,
                "weight": 250
            },
            {
                "name": "Kofe",
                "price": 100,
                "available": False,
                "weight": 250
            },
            {
                "name": "chai",
                "price": 70,
                "available": True,
                "weight": 50
            }
        ]
    }
    with open('products.json', 'w') as file:
        json.dump(products, file)

    with open('products.json', 'r') as file:
        data = json.load(file)

    for i in data["products"]:
        print(
            f'nazv: {i["name"]}\n'
            f'cena: {i["price"]}\n'
            f'ves: {i["weight"]}\n'
            f'{"v nalichii" if i["available"] else "net v nalichii"}\n'
        )

z1()
def z2():
    with open('products.json', 'r') as file:
        exists_data = json.load(file)
print('vvedite dannie: nazvane,cena,ves,v nalichii')
new_data = input().split(',')
exists_data['products'].append(
    dict(
     name=new_data[0],
     price=new_data[1],
     weight=new_data[2],
     available=bool(new_data[3])
    )
)
with open('products.json', 'w') as file:
    json.dump(exists_data, file)
for i in exists_data['products']:
    print(
        f'Nazv: {i["name"]}\n'
        f'cena: {i["price"]}\n'
        f'ves: {i["weight"]}\n'
        f'{"v nalichii" if i["available"] else "net v nalichii"}\n'
    )
z2()
def n2():
import cvs    
    with open('en-ru.txt','r',encoding='utf-8') as file:
        reader = cvs.reader(file, delimiter='-')
        result = sorted(
            [row[::-1] for row in reader],
            key-lambda word:word[0]
        )
    with open('ru-en.txt', 'w', encoding='utf-8') as file_output:
        writer = cvs.writer(file_output, delimiter='-')
        [writer.writerow(data) for data in result]    
n2()