from PIL import Image ,ImageDraw, ImageFont

def z1():
    im = Image.open('9may.jpg')
    im2 = im.crop((20,20,440,440))
    im2.show()
    im2.save('im2.JPG')
z1()

def z2():
    otk = {"день победы":"9may.jpg", "международный женский день":"8mart.jpg", "новый год":"ng.jpg"}
    k =input("Какой праздник?")
    if k in otk:
        image = Image.open(otk[k])
        image.show()
    else:
        print("net otkritki")
z2()
def z3():
    name = input("vvedite imia:")
    filename = "dr.jpg"
    with Image.open(filename) as img:
        img.load()
        font = ImageFont.truetype("Sequência.otf", 30)
        draw_text = ImageDraw.Draw(img)
        draw_text.text(
            (img.width // 2 - 100, 15),
            name + ",pozdravlau!",
            font=font,
            fill=('red')
        )
        img.show()
        img.save(name + "birth2.png")
z3()

