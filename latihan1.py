nama = input("masukan nama  :")
nim = input("masukan nim    :")
a = int(input("masukan Bilngan A 	:"))
b = int(input("masukan Bilangan B 	:"))
c = int(input("masukan Bilangan C 	:"))


angka = [a,b,c]
hasil = max(angka)

print(" ")
print("............................")
print("")

if a>b and a>c:
	huruf = "A"
elif b>c and b>a:
	huruf = "B"
elif c>a and c>b:
	huruf = "C"
else:
	huruf = "A,B,C"


print("\nnama			:",nama)
print("nim				:",nim)
print("Bilangann Terbesar Adalah		:",huruf)
print("Dengan Nilai		:",hasil)