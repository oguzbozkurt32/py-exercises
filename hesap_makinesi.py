print("""****************************
Bu bir hesap makinesidir.

İşlemler:

1)Toplama İşlemi

2)Çıkarma İşlemi

3)Çarpma İşlemi

4)Bölme İşlemi

****************************
""")
a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

işlem = input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} nin toplamı {}dir.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} nin farkı {}dir.".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} nin çarpımı {}dir.".format(a,b,a*b))
elif işlem == "4":
    print("{} nin {} ile bölümü {}dir.".format(a,b,a/b))
else:
    print("Error")