def kwadraten_som(grondgetallen):
    legelijst=[]
    for getal in grondgetallen:
        if getal > 0:
            legelijst.append(getal*getal)

    return sum(legelijst)



kwadraatlijst= [4,5,3,-81]
print(kwadraten_som(kwadraatlijst))