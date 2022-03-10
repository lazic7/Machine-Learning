import math

unosi = []
pBr = 0

while True:

    unos = input("Unesite zeljeni broj, za izlaz iz petlje unestite 'done': ")

    if unos == "done" :
        break

    try:
        unos = float(unos)
        unosi.append(unos)
    except:
        continue

    

sum = sum(unosi)
avg = sum / len(unosi)
print("Srednja vrijednost unesenih brojeva je: ", avg)
print("Min vrijednost unesenih elemenata je: ", min(unosi))
print("Max vrijednost unesenih elemenata je: ", max(unosi))