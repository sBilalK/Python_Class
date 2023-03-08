with open("C:/Users/Win10/Documents/VSCode/Python/MYP/3.Svy/ders3_s3/data.txt", "r", encoding="utf-8") as file:
   veri = file.readlines()
#   for i in veri:
#      print(i)
#print(veri)
for i in range(len(veri)):
   veri[i]=str(veri[i]).rstrip("\n")

#for i in veri:
#   print(i)

sorular = {}
secenekler = []
sayac = 0
for i in range(len(veri)//5):
   Nveri = veri[sayac].split(":")
   sorular.update({Nveri[0]:Nveri[1]})
   secenek_list = []
   for i in range(1,5):
      secenek_list.append(veri[sayac+1])
   sayac += 5
   secenek_list.append(secenek_list)
print(sorular)