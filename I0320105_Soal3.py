# Soal 3
# Membuat program untuk menentukan bilangan prima pada suatu interval
print('PROGRAM MENENTUKAN BILANGAN PRIMA/TIDAK PADA SUATU INTERVAL')
print()
bilangan = 24

for i in range (10, bilangan + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                print(i, 'bukan bilangan prima.')
                break
        else:
            print(i, 'adalah bilangan prima.')

