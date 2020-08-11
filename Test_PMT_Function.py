r = float(input("R: "))
n = float(input("n: "))
e = float(input("e: "))
r= r/1200
p = float(e * (((1+r)**n) -1)) / float(r * ((1+r)**n))
p = round(p,2)
print(p)
