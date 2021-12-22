import time as tm
def decod():
    data = []
    with open('result.txt', 'r') as file:
        for line in file:
            data.append(line)
    # print(data)


    text = open("decoded.txt")
    uncode = text.read()

    uncode = uncode.split()
    text.close()


    # print(uncode)

    def decode_key(data):
        full_key = str(data)
        # print(type(full_key))
        str_key = full_key[23:42]
        # print(str_key)
        t = tm.strptime(str_key, '%Y-%m-%d %H:%M:%S')
        # print(t)
        unix_time = tm.mktime(t)
        key = "".join(str(int(unix_time)))
        key = key * 10
        print(key)
        return (key)


    key = decode_key(data[1])
    print(key)

    # Читаем файл с секретным сообщением
    message = open("result.txt")
    mes = message.read()
    message.close()
    mes = mes.split()


    print(mes)

    # Читаем файл с секретным сообщением


    def shifr(key, uncode, mes):
        for z in range(0, 1):

            try:
                sep = ' '
                x = int()
                q = int(0)
                count = int(0)
                for i in range(0, 100):

                    p = int(key[i])
                    # print("p=", p)
                    if i == 0:
                        x = int(key[i])
                    else:
                        if p == q:
                            x = x + 1
                            print("Здесь х=0")
                        else:
                            x = x + int(key[i])
                            # print(mes[x])
                    uncode[i] = mes[x] + sep
                    count = count + 1
                    
                    if mes[x] == '!':
                        print(uncode[0:count])
                        #print(count)
                        print("Читать закончил")
                        break

                    else:
                        pass
                            #print(uncode[0:count])


            # file.writelines(key)

            except IndexError:
                print('ТЫ ТУПОЙ')
                print(uncode)

        print('ЗАПИСЫВАЮ ДЕШИФРОВКУ')
        with open('uncoded.txt', 'w') as file:
            file.writelines(uncode[0:count])
            print(count)

    shifr(key, uncode, mes)
decod()