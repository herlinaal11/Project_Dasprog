
print('')
print('==========================++ Kalkulator Kesehatan ++==========================')
print('')

print('Hi! Mari menghitung seberapa sehat kondisi tubuh mu ')
print('')
nama    = input('Silahkan Masukan Nama anda : ')
jk      = input('Apa Jenis Kelamin Anda ? Laki-laki / Perempuan : ')
usia    = int(input('Berapa Usia Anda : '))
tinggi  = int(input('Berapa Tinggi Badan anda (cm) : '))
berat   = int(input('Berapa Berat Badan anda (kg) : '))
print('')

print('Baik',nama, 'Silahkan pilih apa yang ingin anda ketahui ?')
print('1. Body Mass Index ')
print('2. Kebutuhan Kalori dalam sehari ')
print('3. Ideal Body Weight ')

print('')
choice = input('Masukan Pilihan anda [1/2/3] : ')
print('')

#BMI
def calc_bmi(berat, tinggi): #fungsi kumpulan perintah atau baris dari BMI
    bmi = float(berat / (tinggi*tinggi/10000))
    if bmi <= 18.4:
        print("Kurang, Ayo Tingkat berat Badan dengan cara yang sehat ! ")
    elif bmi <= 22.9:
        print("Normal, Jaga Kesahatan dan minum air putih yang cukup ! ")
    elif bmi <= 24.9:
        print("Berlebih, Ayo Olahraga ! ")
    elif bmi <= 29.9:
        print("Obesitas Tingkat I , Yuk Menjaga Pola Makan ! ")
    else :
        print("Obesitas Tingkat II , Yuk Mulai atur kalori dan Olahraga yang rutin ! ")

if choice == '1' :
    bmi     = float(berat / (tinggi*tinggi/10000))
    result  = calc_bmi(berat, tinggi)
    
    print('')
    print('Berat Anda = ',+berat)
    print('Tinggi Anda = ',+tinggi)
    print('Hasil Perhitungan Body Mass Index adalah ', +(round(bmi,2)))
    print('Keterangan dari hasil Body Mass Index anda adalah ', result)
    print('')

elif choice == '2':
    if jk == 'Laki-laki':
        rumus   = float(66 + 13.7*berat) 
        rumus1  = float(5*tinggi) - (6.8*usia)
        rumus2  = float(rumus+rumus1)

    else :
        rumus   = float(65.5 + 9.6*berat)
        rumus1  = float(1.7*tinggi) - (4.7*usia)
        rumus2  = float(rumus+rumus1)
    
    print('')
    print('Halo ', nama)
    print('Kalori yang anda butuhkan sebanyak', +rumus2)
    print('')

elif choice == '3':
    if jk == 'Laki-laki' :
        rms1 = int(tinggi) - 100
        rms3 = 0.10 * rms1
        rms4 = rms1 - rms3

    else:
        rms1 = int(tinggi) - 100
        rms3 = 0.15 * rms1
        rms4 = rms1 - rms3
   
    print('')
    print('Halo', nama)
    print('Tinggi Anda adalah',+tinggi, 'Cm')
    print("Berat Badan Ideal untuk Tinggi Badan anda adalah ", rms4 ,"Kg")
    print('')

else :
    print('kosong')

print('==============================++ Terima Kasih ++==============================')
