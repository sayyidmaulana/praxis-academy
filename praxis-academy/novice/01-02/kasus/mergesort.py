'''
Fungsi berikut mengurutkan bilangan pada list menggunakan algoritma merge sort
'''
def merge_sort(list_bilangan):
  jumlah_bilangan =  len(list_bilangan)
  if jumlah_bilangan > 1:
    posisi_tengah = len(list_bilangan)//2
    potongan_kiri = list_bilangan[:posisi_tengah]
    potongan_kanan = list_bilangan[posisi_tengah:]
    
    merge_sort(potongan_kiri)
    merge_sort(potongan_kanan)

    jumlah_bilangan_kiri = len(potongan_kiri)
    jumlah_bilangan_kanan = len(potongan_kanan)
    c_all,c_kiri,c_kanan = 0,0,0 # pencacah/counter
    print('Sebelum merge:',list_bilangan)  
    print('Potongan sebelum merge:',potongan_kiri,':',potongan_kanan)
    while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
      if c_kiri == jumlah_bilangan_kiri: # elemen di potongan kiri habis
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      elif c_kanan == jumlah_bilangan_kanan: # elemen di potongan kanan habis
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]: # nilai elemen di potongan kiri lebih kecil
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      else: # nilai elemen di potongan kanan lebih besar
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      c_all = c_all + 1
    print('Setelah merge:', list_bilangan)
    print()
          
angka = [6,5,3,1,8,7,2,4]
print('Sebelum sort:',angka)
merge_sort(angka)
print('Setelah sort:',angka)

# animasi https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif