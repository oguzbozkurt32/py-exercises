#1 Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

a=int(input("Bir sayı girin:"))

sayı=0
for i in range(1,a):
    if (a%i==0):
        sayı += i
        if sayı==a:
            print("Girdiğiniz sayı mükemmeldir")
        else:
            print("Değildir")

#2 Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

b=int(input("Bir sayı girin:"))

sayı3=0
sayı4=0

if len(str(b))<3 or len(str(b))>4:
    print("Hatalı giriş yaptınız")
elif len(str(b))==3:
    x = list(str(b))
    for i in x:
        sayı3 += int(i) ** 3
    if sayı3==b:
        print("Armstrong sayıdır")
    else:
        print("Normal sayıdır")
elif len(str(b))==4:
    x = list(str(b))
    for i in x:
        sayı4 += int(i) ** 4
    if sayı4==b:
        print("Armstrong sayıdır")
    else:
        print("Normal sayıdır")

#3 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

for i in range(1,11):
    for x in range(1,11):
        print(i*x)



#4 Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
# Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

toplam=0
while True:
    y = input("Bir sayı girin:")
    if y=="q":
        print(toplam)
        break
    else:
        y=int(y)
        toplam+=y

#5 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

i=0

while(i<101):
    if(i%3!=0):
        i+=1
        continue
    print(i)
    i+=1

#6 List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

liste=list(range(0,100))
liste1=list()
for i in liste:
    if i%2==0:
        liste1.append(i)
print(liste1)

