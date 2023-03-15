#1
import testkaynak as tk
import random
import os
# tk.sorular, # tk.secenekler
# for i in tk.sorular:
#     print(i)
indeksler = []
cevaplar = []
sorular = []    
secenekler= []
durum = 1

def Quiz():
    # LİSTE OLARAK TÜM VERİLER ALINACAK VE RANDOM SORU ÇEKİLECEK.      
    while True:
        os.system("cls")
        sorular.clear()
        cevaplar.clear()
        durum = 1
        for key in tk.sorular.keys():
            sorular.append(key)
            cevaplar.append(tk.sorular[key])
            secenekler = tk.secenekler
        # print(sorular) # sorular tamam
        # print(cevaplar) # cevaplar tamam
        # print(secenekler) # secenekler tamam
        tahminler = []
        soruNumber = 1
        dogruCevapSayisi = 0         
        soruSayisi = int(input("Kaç soruluk bir test oluşturmak istersiniz ..").upper())
        if soruSayisi>len(sorular):
            print("HAVUZDA İSTENİLEN KADAR SORU BULUNMAMAKTADIR...")
            print("EN FAZLA ",len(sorular),"SORULUK TEST OLUŞTURABİLİRSİNİZ...")            
            durum = 0
            break           
        else:
            copy_sorular = sorular.copy()
            copy_cevaplar = cevaplar.copy()
            copy_secenekler = secenekler.copy()
            indeksler.clear()
            dogruCevapSayisi=0
            for i in range(soruSayisi):
                soruMetni =random.sample(copy_sorular,1) # sample bir list döndürüyor.
                # sorular.index(soruMetni) hata veriyor.
                indeksNo = copy_sorular.index(soruMetni[0])
                indeksler.append(sorular.index(soruMetni[0]))
                print(copy_sorular[indeksNo])
                for i in copy_secenekler[indeksNo]:
                    print(i)
                tahmin = input("CEVABINIZ A - B - C - D :").upper()
                tahminler.append(tahmin)   
                dogruCevapSayisi+=cevapKontrol(cevaplar[sorular.index(soruMetni[0])],tahmin)
                soruNumber+=1
                # print(dogruCevapSayisi)
                # print(copy_cevaplar[indeksNo])
                copy_sorular.remove(copy_sorular[indeksNo])
                copy_secenekler.remove(copy_secenekler[indeksNo])
                copy_cevaplar.remove(copy_cevaplar[indeksNo])
            break
    if durum == 1:
        sonucGoster(dogruCevapSayisi,tahminler)                
                
def cevapKontrol(cevap,tahmin):
    if cevap==tahmin:
        print("TEBRİKLER BİLDİNİZ...")
        return 1
    else:
        print("ÜZGÜNÜM BİLEMEDİNİZ...!!!")
        return 0

def sonucGoster(dogruCevapSayisi,tahminler):
    print("-"*25)
    print("YARIŞMA SONUCUNUZ")
    print("-"*25)
    print("DOĞRU CEVAPLAR ",end="")
    #for i in sorular:
        #print(sorular.get(i),end=" ") # Bu şekildede olabilir.
    for i in indeksler:
        print(cevaplar[i],end=" ")
    # for i in tk.sorular.values():
    #     print(i,end= " ")
    print()
    print("TAHMİNLERİNİZ  ",end="")
    for i in tahminler:
        print(i,end=" ")
    print()
    print("Doğru cevap sayısı :",dogruCevapSayisi)
    print("Tahminler listesi : ",tahminler)
    puan = (100 // len(tahminler)*dogruCevapSayisi)
    print("Puanınız : ",puan)


def quizDevam():
    secim = input("Devam Etmek İstiyormusunuz (E - H) : ").upper()
    if secim=="E":
        return True
    else:
        return False

Quiz()

while (quizDevam()):
    Quiz()

print("KATILDIĞINIZ İÇİN TEŞEKKÜRLER...")












              
"""
d = {"Massa": 50, "Hamilton": 34, "Vettel": 15, "Alonso": 34}

s = sorted(d.items(), key=lambda x: x[1], reverse=True)

for i in s:
    print("{} {}".format(i[0], i[1])) """


"""
    tahminler = []
    soruNumber = 1
    dogruCevapSayisi = 0   
    for soru in tk.sorular.keys():
        print(str(soruNumber)+".SORU "+"*"*25)
        print(soru)        
        #print(secenekler[soruNumber]) ['A. list', 'B. double', 'C. str', 'D. int'] ekrana gelir.
        #soruNumber+=1
        for i in tk.secenekler[soruNumber-1]:
            print(i)
        tahmin = input("CEVABINIZ A - B - C - D :").upper()
        tahminler.append(tahmin)   
        dogruCevapSayisi+=cevapKontrol(tk.sorular.get(soru),tahmin)
        soruNumber+=1
        print(dogruCevapSayisi)
    sonucGoster(dogruCevapSayisi,tahminler)
"""
