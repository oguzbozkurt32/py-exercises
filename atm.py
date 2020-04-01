print("""Bankamatik: Lütfen işlem seçiniz...
1) Bakiye sorgulama
2) Para çekme
3) Para yatırma

Çıkış yapmak için q ya basınız""")

bakiye=1000

while True:
    işlem = input("İşlem seçiniz:")
    if (işlem=="q"):
        print("Görüşmek üzere")
        break
    elif (işlem=="1"):
        print("bakiyeniz {} tl dir".format(bakiye))
    elif (işlem=="2"):
        miktar=int(input("çekmek istediğiniz miktarı girin:"))
        if (bakiye - miktar < 0):
            print("Geçersiz miktar girdiniz")
        bakiye -= miktar
        continue
    elif (işlem=="3"):
        miktar=int(input("miktar giriniz:"))
        bakiye += miktar

    else:
        print("geçersiz işlem")
