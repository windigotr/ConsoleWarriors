import random

savedGame = open("SavedGame.krc","r")

savedList = savedGame.readlines()

HumanHealth = int(savedList[0])
ComHealth = int(savedList[1])
Strike = 0

savedGame.close()

HumanGuard = 0
ComGuard = 0

HumanGuess = 6
ComGuess = 6

HealthPotCount = 0

raund = 0

print("Savaşa Hoş Geldiniz!")
print("\t\t\t\t\t\t\tConsole Warrior version: 0.01")
print("Son oyuna kaldığınız yerden devam etmek ister misini? (Y/N)")


yukle = input()

if yukle == "Y" or yukle == "y":
    HumanHealth = int(savedList[0])
    ComHealth = int(savedList[1])
else:
    HumanHealth = 100
    ComHealth = 100
    print("""
    Oyuna başlamak için öncelikle rakibinizin gücünü seçin!
    1 - KOLAY    ( 50 - 80 Health)
    2 - DENGELİ  ( 75 - 100 Health)
    3 - ZOR      ( 90 - 120 Health)
    4 - UZMAN    ( 110 - 200 Health)



    Oyun esnasında savaştan kaçmak için ' BIRAK ' yazabilirsiniz.
""")

    level = input("Zorluk seviyesi Seçiminiz:   ")

    if level == "1":
        ComHealth = random.randint(50,80)
    elif level == "2":
        ComHealth = random.randint(75,100)
    elif level == "3":
        ComHealth = random.randint(90,120)
    elif level == "4":
        ComHealth = random.randint(110,200)
    else:
        ComHealth = 100
print(""" --- UNUTMA --- 

Oyun Komutları:

PES:\t Arenadan kaçmış olursun. 
HELP:\t Canın azaldığında iksir içerek yardım alabilirsin.
SAVE:\t Maçını kaydedip tekrar kaldığın yerden devam edebilirsin.

""")
print("""
ADINIZI YAZINIZ:
""")

UserName = input("")

while HumanHealth >= 0 and ComHealth >= 0:
    raund += 1
    HumanHealthBar = int(HumanHealth / 10) * "X" + int(10 - HumanHealth /10)  * "-"
    ComHealthBar = int( 10 - ComHealth/10) * "-" + int(ComHealth/10) * "X"

    Strike = random.randint(1,20)

    print("""
     -------------------- {}. Raund başladı! --------------------
     {} {}                                            {} COM
     [{}]                                     [{}]
     ------------------------------------------------------------

     """.format(raund,UserName,HumanHealth,ComHealth,HumanHealthBar,ComHealthBar))

    print("COM kullanıcısına {} gücünde vuruş yapmak üzeresin!".format(Strike))
    ComGuard = random.randint(1,5)

    print("Bilgisayar sayı seçti. Human tahmin edecek.")
    HumanGuess = input("Human Tahmini: 1-5\n\t")

    if HumanGuess == "1" or HumanGuess == "2" or HumanGuess == "3" or HumanGuess == "4" or HumanGuess == "5":
        HumanGuess = int(HumanGuess)

    elif HumanGuess == "PES":
        HumanHealth = -1
    elif HumanGuess == "SAVE":
        SaveGameList = [HumanHealth,ComHealth]

        saveGame = open("SavedGame.krc","w")
        saveGame.write(str(SaveGameList[0])+ "\n" + str(SaveGameList[1]))
        print("Oyun Kaydedildi")
        saveGame.close()
        break
    else:
        print("Iskaladın! ")
        HumanGuess = 1040
    if ComGuard == HumanGuess:
        ComHealth = ComHealth - Strike
        print("Tebrikler, vurdun. COM kullanıcısından {} canı gitti. {} canı kaldı.".format(Strike,ComHealth))
    else:
        if HumanGuess == 1040:
            print("COM kullanıcına hiç vuruş yapamadığın {} canı ile savaşa devam ediyor.".format(ComHealth))
        else:
            print("Bilemedin. COM kullanıcısı {} sayısını seçmişti. Sen {} sayıyı seçtin. COM kullanıcısının canı hala {}".format(ComGuard,HumanGuess,ComHealth))
    if ComHealth < 0:
        print("COM kullanıcısı öldü!")
        break
#   Kodlardaki karakterler yer değiştiriyor.

    print("\nŞimdi vurma sırası COM kullanıcısında!")

    Strike = random.randint(1,20)

    print("COM kullanıcısı sana {} gücünde vuruş yapmak üzere!".format(Strike))

    HumanGuard = input("Seçimini yap!: \n\t")

    if HumanGuard == "1" or HumanGuard == "2" or HumanGuard == "3" or HumanGuard == "4" or HumanGuard == "5":

        HumanGuard = int(HumanGuard)

    elif HumanGuard == "HELP":
        HealthPotCount += 1
        HealthPot = random.randint(0,20)
        HumanHealth += HealthPot
        if HealthPotCount > 3:
            HumanHealth -= 2*HealthPot
        # print("iksiri içtin ve {} can kazandın. Artık {} canın var.".format(HealthPot,HumanHealth))
    elif HumanGuess == "SAVE":
        SaveGameList = [HumanHealth,ComHealth]

        saveGame = open("SavedGame.krc","w")
        saveGame.write(str(SaveGameList[0])+ "\n" + str(SaveGameList[1]))
        print("Oyun Kaydedildi")
        saveGame.close()
        break

    elif HumanGuard == "PES":
        HumanHealth = -1
    # else:
    #     print("CEZA! Hile yaptın ve 15 canın silinecek")
    #     HumanGuard = 1040

    print("Bilgisayar tahmin yapıyor!")
    ComGuess = random.randint(1,5)

    if HumanGuard == ComGuess:
        HumanHealth -= Strike
        print("Malesef vuruldun ve {} canın gitti. Artık {} canın kaldı.".format(Strike,HumanHealth))
    else:
        if HumanGuard == 1040:
            HumanHealth -= 15
            print("Artık {} canın kaldı! Bundan sonra daha dikkatli devam etmelisin.".format(HumanHealth))
        if HumanGuard =="HELP":
            if HealthPotCount < 4:
                print("{}. iksirini içtin ve {} can kazandın. Artık {} canın var.".format(HealthPotCount,HealthPot, HumanHealth))
            else:
                print("iksiri çok içtin ve zehirlendin. {} canın silinecek.".format(HealthPot))
        else:
            print("Kurtuldun! Sen {} sayısını seçmiştin. COM kullanıcısı ise {} sayısını seçti. Senin hala {} canın var!".format(HumanGuard,ComGuess,HumanHealth))

    print("\n"*20)
# Artık savas bitiyor ve sonuc ekranı yazdırılıyor.

print("\n\n Savaş Bitti!")
print("""
     -------------------- {}. Raund Sonucu! --------------------
     {} {}                                            {} COM
     [{}]                                     [{}]
     ------------------------------------------------------------

     """.format(raund, UserName,HumanHealth, ComHealth, HumanHealthBar, ComHealthBar))
if HumanHealth < 0:
    print("""

    ----- KAYBETTİN! -----

    {} FARKLA OYUNU KAYBETTİN.

    """.format(ComHealth-HumanHealth))
else:
    print("""
    ----- KAZANDIN! -----

    {} FARKLA OYUNU KAZANDIN.
    """.format(HumanHealth-ComHealth))

close = ""
while close != "q" or close != "Q":
    print("Oyundan çıkmak için q tuşuna basınız.")
    close = input()
