#umumiy markazga bo'lgan ikkita aylana radiusi berilgan. Ularning yuzalari S1 va S2
# ularning ayirmasi S3 aniqlansin.
r1=float(input("Birinchi aylana radiusini kiriting"))
r2=float(input("Ikkinchi aylana radiusini kiriting"))
P=3.14
S1=P*r1*r1
S2=P*r2*r2
S=S1-S2
print("Birinchi aylana radiusi",r1,"Aylananing yuzasi",S1)
print("Ikkinchi aylana radiusi",r2,"Aylananing yuzasi",S2)
print("Ikki aylananing yuzalari ayirmasi",S)