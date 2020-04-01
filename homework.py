# 1
print("Vücut kitle endeksi hesaplama")

boy=float(input("Boy gir:"))
kilo=int(input("Kilo gir:"))

index = kilo / boy**2

if index > 30:
    print("Obez")
elif index > 25:
    print("Fazla kilolu")
else:
    print("Okeysin")

#2

a=int(input("Birinci sayıyı girin:"))
b=int(input("İkinci sayıyı girin:"))
c=int(input("Üçüncü sayıyı girin:"))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > b and c > a:
    print(c)
else:
    print("Hatalı giriş yaptınız")

#3

print("Harf Notu Hesaplama")

Vize1=int(input("Vize1 notu girin:"))
Vize2=int(input("Vize2 notu girin:"))
Final=int(input("Final notu girin:"))

Harf= Vize1*0.3 + Vize2*0.3 + Final*0.4

if Harf > 90:
    print("AA")
elif Harf > 80:
    print("BA")
elif Harf > 70:
    print("CC")
elif Harf > 60:
    print("DC")
else:
    print("FF")

#4
print("Şekil hesaplamaya hoşgeldiniz...")

Şekil1="Dörtgen"
Şekil2="Üçgen"

Şekil3=input("Şekil giriniz:")

if Şekil1 == Şekil3:
    Kenar1=int(input("Kenar1:"))
    Kenar2=int(input("Kenar2:"))
    Kenar3=int(input("Kenar3:"))
    Kenar4=int(input("Kenar4:"))
    if Kenar1 == Kenar2 == Kenar3 == Kenar4:
        print("Kare")
    elif Kenar1 == Kenar2 and Kenar3==Kenar4 and Kenar1+Kenar2 > Kenar3+Kenar4 or Kenar1 == Kenar2 and Kenar3==Kenar4 and Kenar1+Kenar2 < Kenar3+Kenar4 :
        print("Dikdörtgen")
    else:
        print("Geçersiz kenar uzunluğu girdiniz.")
elif Şekil2 == Şekil3:
    Kenar5=int(input("Kenar5:"))
    Kenar6=int(input("Kenar6:"))
    Kenar7=int(input("Kenar7:"))
    if Kenar5 == Kenar6 == Kenar7:
        print("Eşkenar Üçgen")
    elif Kenar5 == Kenar6 and Kenar5 + Kenar6 > Kenar7 or Kenar7 == Kenar6 and Kenar7 + Kenar6 > Kenar5 or Kenar5 == Kenar7 and Kenar5 + Kenar7 > Kenar6:
        print("İkizkenar Üçgen")

else:
    print("Geçersiz bir şekil girdiniz.")
























