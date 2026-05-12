print("Ohjelma laskee lukujen n, n * (n-1) *...*1")
print()

n = int(input("Anna positiivinen kokonaisluku n: "))

while n <= 0:
    print("Et anna positiivista kokonaisluku")
    n = int(input("Anna positiivinen kokonaisluku n: "))
summa = 1
for luku in range(n, 0, -1):
    summa *= luku
    print("Lukujen summa:", summa)
