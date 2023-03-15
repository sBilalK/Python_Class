with open("C:/Users/Win10/Documents/VSCode/Python/MYP/3.Svy/ders3_s3/data.txt","r",encoding="utf-8-sig") as file:
    veri = file.readlines()
# for i in veri:
#     print(i)
# print(veri)
for i in range(len(veri)):
    veri[i]=str(veri[i]).rstrip("\n")

# for i in veri:
#     print(i)
sorular = {}
secenekler = []
sayac=0
for i in range(len(veri)//5): # range(4)
    yeni_veri = veri[sayac].split(":")
    sorular.update({yeni_veri[0]:yeni_veri[1]})
    secenekler_listem = []
    for i in range(1,5):  # i=1,2,3,4
        secenekler_listem.append(veri[sayac+i])  
    sayac+=5
    secenekler.append(secenekler_listem)
print("Sorular Sözlüğü Oluşturuldu ..:")
print("-"*25)
print(sorular)
print("Seçenekler Listesi Oluşturuldu..:")
print("-"*25)
for i in secenekler:
    print(i)