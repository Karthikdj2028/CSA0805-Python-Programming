# 3. Perfect number check
x=6
pnum=(x==sum(i for i in range(1,x) if x%i==0))
print(f"{x} is a perfect number" if pnum else f"{x} is not a perfect number")