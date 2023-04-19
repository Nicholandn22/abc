buku = open('daftarbuku.txt','r')
nama = input('Masukkan nama buku yang dicari : ')
abc = [nama]
aa = []
bb = []
cc = []
dd = []
for line in buku:
    split = line.split(',')
    nama_buku = split[0].strip()
    kode = split[1].upper()#.split()
    tahun = split[2]#.split()
    deskripsi = split[-1]#.split()
    d = ''.join(nama_buku)
    a = ''.join(kode)
    b = ''.join(tahun)
    c = ' '.join(deskripsi)
    aa.append(nama_buku)
    bb.append(kode)
    cc.append(tahun)
    dd.append(deskripsi)

for i in range(len(aa)):
    if nama == aa[i]:
        print(f'BUKU ditemukan')
        print(f'Nama : {aa[i]}')
        print(f'Kode : {bb[i]}')
        print(f'Tahun Rilis : {cc[i]}')
        print(f'Deskrips : {dd[i]}')

# if nama == aa[0] or nama == aa[1] or nama == aa[2] or nama == aa[3] or nama == aa[4]:
#     print(f'BUKU ditemukan')
#     print(f'Nama : {d}')
#     print(f'Kode : {a}')
#     print(f'Tahun Rilis : {b}')
#     print(f'Deskrips : {c}')
# else :
#     print('Barang tidak ditemukan silahkan mencari lagi')
buku.close()
    
    