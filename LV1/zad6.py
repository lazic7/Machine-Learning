fname = input('Unesite ime datoteke: ') #npr LV1/mbox.txt
substring = "From "
adrese = []
hostnames = []
pBr = 0

dictionary = dict()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    if substring in line:
        words = line.split()
        adrese.append(words[1]) #dodajem "word" sa ideksa 1 u listu "adrese" zato sto ce email adresa bas biti na indexu 1 kad skripta pronadje liniju sa "From "

for adresa in adrese: #za svaku adresu u listi adresa
    for char in adresa: #prodji kroz svaki znak u pojedinoj adresi
        pBr += 1 #pomocni brojac ce mi izbrojati koliko znakova ima do "@" a onda u substring spremim hostname koji ide nakon @
        if char == "@":
            substring2 = adresa[pBr: ] #umjesto [pBr: ] moze ici i [pBr-1: ] kako bi se zahvatio i znak "@" ako to zelimo
            hostnames.append(substring2) #dodajem taj substring u listu hostname-ova

    pBr = 0 #brojac moram vratiti na 0 kako bi za sljedecu adresu iz liste adresa mogao pravilno prebrojati koliko znakova ima do "@"     

for hostname in hostnames: #spremam hostnameove u dictionary
    if hostname not in dictionary:
        dictionary[hostname] = 1
    else:
        dictionary[hostname] += 1

print("\nNeke od email adresa su:\n", adrese[0:5])
print("\nIspis imenika hostnameova: \n",dictionary)
