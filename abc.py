print('========== KALKULATOR CERDAS ==========')
print('Pilihlah bangun yang ingin anda hitung (inputan angka saja) :')
print(' 1. tabung\n 2.Kubus\n 3.balok')
a = int(input('>> '))
def tabung():
    a1 = int(input('Masukkan diameter (cm) : '))
    a2 = int(input('Masukkan tinggi(cm) : '))
    volumet = 3.14 * ((a1/2)**2) * a2
    print(f'Volume tabung adalah {volumet} cm')
def kubus():
    b1 = int(input("masukkan sisi (cm) : "))
    volumek = b1 ** 3
    print(f'Volume kubus adalah {volumek} cm')
def balok():
    c1 = int(input('Masukkan panjang(cm) : '))
    c2 = int(input('Masukkan lebar(cm) : '))
    c3 = int(input('Masukkan tinggi(cm) : '))
    volumeb = c1*c2*c3
    print(f'Volume balok adalah {volumeb} cm')
if a == 1:
    tabung()
elif a == 2:
    kubus()
elif a == 3:
    balok()

