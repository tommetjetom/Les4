def standaardprijs(afstandKM):
    if afstandKM < 0:
        return False
    elif afstandKM > 50 :
       prijs= (afstandKM * 0.60)+ 15
       return prijs
    elif afstandKM < 50:
        prijs = (afstandKM * 0.80)
        return prijs

def ritprijs(leeftijd,weekendrit,afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd > 64 and weekendrit == True:
        eindprijs = prijs * 0.65
        return eindprijs
    elif leeftijd < 12 or leeftijd > 64:
        eindprijs= prijs* 0.7
        return eindprijs
    elif weekendrit == True:
        eindprijs = (prijs * 0.6)
        return eindprijs
    elif weekendrit == False:
        eindprijs = prijs
        return eindprijs
print(ritprijs(13,True,100))
