from PIL import Image, ImageDraw, ImageFont
import random as r
from coding import res_text, coding
#coding()
text = []
def picture():
    with open('result.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.split()
    print('AAAAAAAAA', text)

    images = ['bg1.jpg','bg2.jpg', 'bg3.jpg', 'bg4.jpg', 'bg5.jpg','bg6.jpg', 'bg7.jpg', 'bg8.jpg', 'bg9.jpg','bg10.jpg']
    image = images[r.randint(0,(len(images)))]
    #image = 'bg2.jpg'
    im = Image.open(image)
    #im1 = Image.new('RGBA', (300, 100, 200, 200), color=('#FAACAC'))

    #Настройки вывода текста
    x = 800
    y = 200
    s = 70

    # Создаем объект со шрифтом
    font = ImageFont.truetype('Submarine Beach.ttf', size=130)
    draw_text = ImageDraw.Draw(im)


    n = 0
    numb = 5
    column = []
    draw_text.text(
        (850, 50),
        ''.join('Поздравляем с Днём ВМФ!'),
        # Добавляем шрифт к изображению
        font=font,
        fill='#ff0000')
    font = ImageFont.truetype('Submarine Beach.ttf', size=s)
    for i in range(len(text)//numb):
        column = []
        for j in range(n,n+numb):
            #print(j)
            if text[j] == 'Сообщение':
                break
            else:
                column.append(f'{text[j].center(10)}')

        #print('ffffffffffff', column)
        draw_text.text(
            (x, y),
            ''.join(column),
            # Добавляем шрифт к изображению
            font=font,
            fill='#0000ff')

        n+=numb
        y += 40
    im.show()
    im.save('C днём ВМФ!.jpg')




if __name__ == '__main__':
    picture()