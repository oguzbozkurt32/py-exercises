"""ödev 1
print ("Sayıların Çarpımını Hesaplama")

Sayı1=int(input("Birinci Sayı:"))
Sayı2=int(input("İkinci Sayı:"))
Sayı3=int(input("Üçüncü Sayı:"))

Çarpım=(Sayı1*Sayı2*Sayı3)

print("Sonuç=".format(Çarpım))


ödev2
print ("Vücut Kitle Endeksi")
Boy=int(input("Boy:"))
Kilo=int(input("Kilo:"))

Endeks= Kilo / (Boy/100)**2

print(Endeks)

ödev3

print("Yakıt Ücreti Hesabı")
Lira=float(input("Para:"))
Yol=float(input("KM:"))

Ücret=(Lira*Yol)

print("{}x{}={}".format(Lira,Yol,Ücret))

ödev4

print ("Kullanıcı Bilgileri")
Ad=input("İsim:")
Soyad=input("Soyisim:")
Numara=input("Numara:")

print ("Ad {}\n,Soyad {}\n,Numara")

ödev5

print("Lütfen 2 sayı girin")

Sayı1=int(input("Birinci Sayı:"))
Sayı2=int(input("İkinci Sayı:"))

print("Sayılar yer değiştiriyor sorma neden...")

print("{} ve {}".format(Sayı2,Sayı1) )

ödev6"""

print("Hipotenüs Hesabı")

a=int(input("Birinci kenar:"))
b=int(input("İkinci kenar:"))

C=(a**2+b**2)**0.5

print("Hipotenüs Hesaplanıyor...")

print("Kenarı {} ve {} olan üçgenin hipotenüsü {}dir".format(a,b,C))