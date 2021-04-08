# Soal 2
# Membuat program untuk menghitung nilai rata-rata yang diinputkan
print('PROGRAM MENGHITUNG RATA RATA NILAI \n')
# Memasukkan banyak data
BanyakData = int(input('Banyak data : '))

Data = []
JumlahNilai = 0

# Melakukan pengulangan
for i in range (0,BanyakData):
    DataNilai = int(input('Data Nilai ke-%d : '%(i+1)))
    Data.append(DataNilai)
    JumlahNilai += Data[i]
    RataRata = JumlahNilai/BanyakData
print( )

# Mencetak nilai rata rata
print('Nilai rata-rata = %0.2f' %RataRata)

