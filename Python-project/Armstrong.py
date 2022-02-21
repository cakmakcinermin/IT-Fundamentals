number = input("kullanicidan bir sayi al:")
lenght = len(number)
toplam = 0 
for i in number:
    toplam+=int(i)**lenght
if str(toplam)==number:
    print('Bu sayi armstrong sayisidir')
else: 
    print("Bu sayi bir armstrong sayisidir")
