# 6. GCD and LCM
from math import gcd
lcm=lambda x,y:x*y//gcd(x,y)
lg=lcm(15,20)
gg=gcd(60,48)
print("LCM of 15 and 20 is", lg)
print("The gcd of 60 and 48 is:", gg)