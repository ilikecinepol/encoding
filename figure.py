from PIL import Image, ImageDraw, ImageFont
from coding import coding
import random as r



'''
Координаты текста:
1 строка: 850,50 - 1700,50
2 строка: 850,150-  1700, 150
3 строка: 850
4 Строка: 850
5 Строка: 850
'''
def open_text():

    with open('result.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.split()
    return  text
    #print('AAAAAAAAA', text)

def old_method():
    font = ImageFont.truetype('Submarine Beach.ttf', size=130)

    x = 800
    y = 200
    s = 70

    draw_text = ImageDraw.Draw(im)


    n = 0
    numb = 5
    column = []
    draw_text.text(
        (850, 150),
        ''.join('Н'),
        # Добавляем шрифт к изображению
        font=font,
        fill='#ff0000')
    draw_text.text(
        (1700, 150),
        ''.join('К'),
        # Добавляем шрифт к изображению
        font=font,
        fill='#ff0000')
    im.show()
    im.save('C днём ВМФ!.jpg')


def figure():
    pass



def cat_word(number, word, im):
    #image = 'word.png'
    #im = Image.open(image)

    text = word.upper()
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype('Submarine Beach.ttf', size=72)
    draw_text.text(
        (0, 0),
        ''.join(text.ljust(0)),
        # Добавляем шрифт к изображению
        font=font,
        fill='#0000ff')

    #im.show()
    im.save(f'word_{number}.png')

def new_method():

    text = open_text()
    print(text)

    for i in range(len(text)):
        img = Image.new('RGBA', (35 * len(text[i]), 72))

        cat_word(i, text[i], img)


fig = '''
*****
*****
*****
*****
*****   
'''
def figure():
    images = ['bg1.jpg', 'bg2.jpg', 'bg3.jpg', 'bg4.jpg', 'bg5.jpg', 'bg6.jpg', 'bg7.jpg', 'bg8.jpg', 'bg9.jpg',
              'bg10.jpg']
    #image = images[r.randint(0, (len(images)))]


    image = 'bg2.jpg'
    img = Image.open(image)
    img.convert('RGBA')
    img.save(f'{image}.png')
    image = f'{image}.png'
    img = Image.open(image)

    x = 850
    y = 200
    n = 0
    h = 210 #Ширина каждого слова в px
    for i in range(10):
        try:
            for j in range(5):
                im1 = Image.open(f'word_{n}.png')

                resized = im1.resize((h, 100))
                resized.save(f'word_{n}.png')

                im1 = Image.open(f'word_{n}.png')
                img.paste(im1, (x, y), im1)
                n += 1
                x += 160
            x = 850
            y += 75
        except FileNotFoundError:
            pass

    im1 = Image.open('word_2.png')

    #im.paste(im1, (850,150))
    img.show()
    img.save("Открытка.jpg")






if __name__ == '__main__':
    coding()

    new_method()

    figure()

