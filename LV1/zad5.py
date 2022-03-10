def avg_reliability(): #ovo je funkcija koja ce obaviti izracun
    
    fname = input('Unesite ime datoteke: ') #npr. c:/Users/user/Desktop/PSU_LV/LV1/mbox.txt
    substring = "X-DSPAM-Confidence: "
    substring_lenght = len(substring)
    vrijednosti = [] 

    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    for line in fhand:
        if substring in line:

            try:
                vrijednost = float(line[substring_lenght: ])
                vrijednosti.append(vrijednost)
            except:
                exit()

    avg = sum(vrijednosti) / len(vrijednosti)
    print("Srednja vrijednost pouzdanosti: ", avg)

avg_reliability() 
avg_reliability()        
        
