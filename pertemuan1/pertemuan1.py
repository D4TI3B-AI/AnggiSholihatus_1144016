import time
mulai_waktu = time.time()
print("Menghitung (Jumlah Hasil)")
m = raw_input("Masukan angka m : ")
a = raw_input("masukan angka a : ")
b = raw_input("Masukan angka b : ")
c = raw_input("Masukan angka c : ")
if m == 'satu':
	m=1
if m == 'dua':
	m=2
if m == 'tiga':
	m=3
if m == 'empat':
	m=4
if m == 'lima':
	m=5
if m == 'enam':
	m=6
if m == 'tujuh':
	m=7
if m == 'delapan':
	m=8
if m == 'sembilan':
	m=9
if m == 'nol':
	m=0


if a == 'satu':
	a=1
if a == 'dua':
	a=2
if a == 'tiga':
	a=3
if a == 'empat':
	a=4
if a == 'lima':
	a=5
if a == 'enam':
	a=6
if a == 'tujuh':
	a=7
if a == 'delapan':
	a=8
if a == 'sembilan':
	a=9
if a == 'nol':
	a=0

if b == 'satu':
	b=1
if b == 'dua':
	b=2
if b == 'tiga':
	b=3
if b == 'empat':
	b=4
if b == 'lima':
	b=5
if b == 'enam':
	b=6
if b == 'tujuh':
	b=7
if b == 'delapan':
	b=8
if b == 'sembilan':
	b=9
if b == 'nol':
	b=0

if c == 'satu':
	c=1
if c == 'dua':
	c=2
if c == 'tiga':
	c=3
if c == 'empat':
	c=4
if c == 'lima':
	c=5
if c == 'enam':
	c=6
if c == 'tujuh':
	c=7
if c == 'delapan':
	c=8
if c == 'sembilan':
	c=9
if c == 'nol':
	c=0
Jumlah = (m*a)+(b/c)
print("Jumlah Perhitungan", Jumlah)
print("Waktu Menghitung : %s detik " % (time.time() - mulai_waktu))