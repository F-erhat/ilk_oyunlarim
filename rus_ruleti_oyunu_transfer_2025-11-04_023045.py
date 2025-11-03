import random
import time

def rus_ruleti_oyna():
    print("=============================================", flush=True)
    print("      🔫 RUS RULETİ: TEHLİKELİ OYUN 🔫", flush=True)
    print("=============================================", flush=True)
    time.sleep(1.5)
    
    toplam_hazne=int(input("Oyunumuzda ki tabancanın şarjörü kaç mermilik olsun?"))
    mevcut_hazne=1
    mermi_konumu= random.randint(1,toplam_hazne)
    olme_ihtimali= 100/toplam_hazne
    
    print(f" \n Silah kapasitesi {toplam_hazne} mermiyi kapsıyor. Ölme ihtimalin %{olme_ihtimali} Mermi rastgele konumlandırılıyor. Bol şans!")
    time.sleep(2)
    
    while mevcut_hazne <= toplam_hazne:
        print("\n ----------------------------------------------------", flush=True)
        time.sleep(1)
        if mevcut_hazne %2 != 0:
            oyuncu = "SİZ"
        else:
            oyuncu = "PC"
            
        print(f"Sıra: {oyuncu}",flush=True)
        print(f"Mevcut hazne: {mevcut_hazne}",flush=True)
        time.sleep(1)
        
        if mevcut_hazne == mermi_konumu:
            time.sleep(1.5)
            print("💀 BOOM! 💀")
            time.sleep(1)
            if oyuncu == "SİZ":
                print("\n KAYBETTİNİZ - Azrail'den kurtuluşun yok.")
            else:
                print("\n KAZANDINIZ - Çok şanslısınız")
            
            print("\n ====================================================" ,flush=True)
            return
        else:
            print("...TIK...")
            time.sleep(2)
            print(f"Çok şanslısınız. {mevcut_hazne} hazne boştu.")
            mevcut_hazne +=1
    print(" \n Oyun bitti! Silindirde mermi yoktu.")
    
rus_ruleti_oyna()

while True:
    tekrar = input(" \n Tekrar oynamak ister misiniz? E/H").lower()
    if tekrar == 'e':
        rus_ruleti_oyna()
    elif tekrar == 'h':
        print("\n Oynadığınız için teşekkür ederiz. Ölene kadar tekrar bekleriz :)")
        break
        
    else:
        print("Lütfen E ya da H ye basın!")
    
            