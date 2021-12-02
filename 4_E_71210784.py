m = [3, 20, 90 ,35, 75]

def besar(deret):
    terbesar = deret[0]
    for i in deret:
        if i > terbesar:
            terbesar = i
    return terbesar

def kecil(deret):
    terkecil = deret[0]
    for i in deret:
        if i < terkecil:
            terkecil = i
    return terkecil

print(m)
print("Angka terbesar adalah : ", besar(m))
print("Angka terkecil : ", kecil(m))
