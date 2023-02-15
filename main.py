def Shifrator():
    Simvols1 = "QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?qwertyuiop[]asdfghjkl;'zxcvbnm,.ЙЦУКЕНГШЩЗХ ЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю\/1234567890-=!№%*()_+@#$^&"
    Simvols1 = str(Simvols1)
    Simvols2 = "ZcY$IynЖ:\"DиИаЧ?CШЭДЛ5mdБр&pгqмС2gшLФfAхЦ9[уP!{ЩzАwПTЬв=цrпR'\ф}УN-XЫч%йзvо,#<ЙЪiГю08xР7k3^бEьVGoh1>тжjнFSs6tсlОк4OJb@ЕКaщэeHН _MB;/ы.яМW)З+лдQТЮХЯъ]№(е*ВKUu"
    Simvols2 = str(Simvols2)

    print("Зашифровать напишите 0 \nДешифровать напишите 1")
    What = input()
    if (What == '0'):
        print("Напишите текст")
        Text = input()
        itog = ''
        for i in Text:
            mesto = Simvols1.find(i)
            new_buckva = Simvols2[mesto]
            itog += new_buckva
        print(itog)
    else:
        print("Напишите текст")
        Text = input()
        itog = ''
        for i in Text:
            mesto = Simvols2.find(i)
            new_buckva = Simvols1[mesto]
            itog += new_buckva
        print(itog)

if __name__ == '__main__':
    Shifrator()