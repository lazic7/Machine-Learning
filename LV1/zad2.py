try:
    x = 0

    while True:
        
        x=float(input("Unesite velicinu ocijene [0.0 - 1.0]: "))

        if x >= 0.0 and x<=1.0:
            break
        else:
            print("Pogresno unesena velicina!")
            

    if x>= 0.9 and x<=1.0:
        print("A")
    elif x>=0.8 and x<0.9:
        print("B")
    elif x>=0.7 and x<0.8:
        print("C")
    elif x>=0.6 and x<0.7:
        print("D")
    elif x<0.6 and x>=0.0:
        print("F")
    
        
except:
    print("An exception occurred")