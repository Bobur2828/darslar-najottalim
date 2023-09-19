#Paralelepedning tomonlari a,b,c tomonlari berilgan. Uning hajmini va to'la sirtini aniqlansin.
a=float(input("Paralelepedning a tomonini kiriting")) 
b=float(input("Paralelepedning b tomonini kiriting"))
c=float(input("Paralelepedning c tomonini kiriting"))
V=a*b*c
S=2*(a*b+b*c+a*c)
print("Paralelepedning hajmi",V ,"Paralelepedning to'la sirti esa",S)