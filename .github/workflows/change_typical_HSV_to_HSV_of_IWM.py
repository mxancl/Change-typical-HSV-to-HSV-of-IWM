print("use this website to get H,S,V: https://c.runoob.com/front-end/868/")
print("to use this program, you need to install Python and search IDLE in Search bar, open it, than click File and choose Open... click this file and press F5.") 
H,S,V=(input("input H,S,V in order,the result successively is H,S,V in IWM, use one space to split H,S and V").split())
H=float(H)
S=float(S)
V=float(V)
h=round(H*180)
t=S*4
from decimal import Decimal
s=Decimal(t).quantize(Decimal("0.01"),rounding="ROUND_HALF_UP")
print(h,s,'{:.0%}'.format(V))
