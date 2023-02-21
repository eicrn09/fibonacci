isim=input("isminizi girin:   ")
noktasayisi=0

while noktasayisi<100:
    print('.')
    noktasayisi+=1

print( "merhaba,"+isim)

hisse=input('Hesaplama yapmak istediginiz hisse: ')
yd=str(input('Hisse yukselen trendde mi dusen trendde mi: '))

if yd=='yukselen':
    y=float((input('yuksek: ')))
    d=float((input('dusuk: ')))   
    deger1=float(0.236)
    a=int(y-d)
    print('23,6%'+'='+str(a*deger1+y))

    deger=float(0.382)
    a=int(y-d)
    print('38,2%='+ str(a*deger+y))

    deger3=float(0.50)
    a=int(y-d)
    print('50%='+str(a*deger3+y))

    deger4=float(0.618)
    a=int(y-d)
    print('61,8%='+ str(a*deger4+y))

    deger5=float(1)
    a=int(y-d)
    print('100%='+ str(a*deger5+y))

    deger6=float(1.382)
    a=int(y-d)
    print('138,2%='+ str(a*deger6+y))

    deger9=float(1.618)
    a=int(y-d)
    print('161,8%='+ str(a*deger9+y))

    deger7=float(2)
    a=int(y-d)
    print('200%='+ str(a*deger7+y))

    deger8=float(2.618)
    a=int(y-d)
    print('261,8%='+ str(a*deger8+y))

else:
    y=float((input('yuksek: ')))
    d=int((input('dusuk: ')))
    deger1=float(0.236)
    a=int(y-d)
    print('23,6%'+'='+str(d-a*deger1))

    deger2=float(0.382)
    a=int(y-d)
    print('38,2%'+'='+str(d-a*deger2))

    deger3=float(0.50)
    a=int(y-d)
    print('50%='+str(d-a*deger3))

    deger4=float(0.618)
    a=int(y-d)
    print('61,8%='+ str(d-a*deger4))

    deger5=float(1)
    a=int(y-d)
    print('100%='+ str(d-a*deger5))

    deger6=float(1.382)
    a=int(y-d)
    print('138,2%='+ str(d-a*deger6))

    deger9=float(1.618)
    a=int(y-d)
    print('161,8%='+ str(d-a*deger9))

    deger7=float(2)
    a=int(y-d)
    print('200%='+ str(d-a*deger7))

    deger8=float(2.618)
    a=int(y-d)
    print('261,8%='+ str(d-a*deger8))


