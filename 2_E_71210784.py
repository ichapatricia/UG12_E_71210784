x = str(input("Hi Tutu, silahkan masukan hari yang ingin anda telusuri: " ))

senin = ['ke-1 Algoritma Graf','ke-3 Sistem Operasi', 'ke-4 PAK',' ke-5 Praktikum INLAN']
selasa = ['ke-2 Matematika Teknik', 'ke-4 Bhs Indonesia', 'ke-6 PKN']
kamis = ['ke-1 IMK', 'ke-3 Logmat','ke-4 Praktekkom']
jumat = ['ke-2 Sistem Basis Data', ' ke-4 Praktikum Basis Data','ke-6 INLAN']

if x == "senin":
    for i in range(len(senin)):
        print("Kelas", senin[i])
elif x == "selasa":
   for i in range(len(selasa)):
         print("Kelas", selasa [i])
elif x ==  "rabu":
         print("Hari rabu anda tidak ada kelas!")
elif x == "kamis":
    for i in range(len(kamis)):
         print("Kelas", kamis[i])
elif x ==  "jumat":
    for i in range(len(jumat)):
         print("Kelas", jumat[i])
