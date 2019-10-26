print ("")
print ("------ PROGRAM PYTHON UNTUK MENGHITUNG SALDO ------")
print ("")
print ("")

tabungan = int(input("Masukkan jumlah tabungan :"))
lama = int(input("Masukkan jumlah lama menabung (bulan) :"))
 
if tabungan < 1000000 :
 sukuBunga = 0.03
 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
 print("")
 print("Karena tabungan anda dibawah 1.000.000, bunga yang anda dapatkan adalah 3%")
 print("")
 print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))
 
elif tabungan > 1000000 :
 sukuBunga = 0.04
 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
 print("")
 print("Karena tabungan anda diatas 1.000.000, bunga yang anda dapatkan adalah 4%")
 print("")
 print("Maka setelah menabung selama " + str (lama) + " bulan, saldo anda adalah " +str (saldoAkhir))
