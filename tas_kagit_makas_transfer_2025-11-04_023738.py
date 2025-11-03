import random
tas="Taş"
kagit= "Kağıt"
makas= "Makas"
liste=("Taş","Kağıt","Makas")

pc_puani=0
oyuncu_puani=0

while True:
    kullanici_cevabi = input("Cevabınız: ")
    pc_secimi= random.choice(liste)
    if kullanici_cevabi.upper() == tas.upper():
        if pc_secimi.upper() == tas.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Berabere")
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        elif pc_secimi.upper() == kagit.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Bilgisayar kazandı!")
            pc_puani=pc_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        else:
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Sen kazandın!")
            oyuncu_puani=oyuncu_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print('Bilgisayarın puanı: ',pc_puani)
            print("")
    elif kullanici_cevabi.upper() == kagit.upper():
        if pc_secimi.upper() == tas.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Sen kazandın!")
            oyuncu_puani=oyuncu_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        elif pc_secimi.upper() == kagit.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Berabere!")
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        else:
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Bilgisayar kazandı!")
            pc_puani=pc_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
    else:
        if pc_secimi.upper() == tas.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Bilgisayar kazandı!")
            pc_puani=pc_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        elif pc_secimi.upper() == kagit.upper():
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Sen kazandın!")
            oyuncu_puani=oyuncu_puani+1
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("")
        else:
            print(f"Bilgisayar {pc_secimi} seçti.")
            print("Berabere!")
            print("Senin puanın: ", oyuncu_puani)
            print("Bilgisayarın puanı: ",pc_puani)
            print("") 