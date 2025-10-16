# 5. Mth max, Nth min, sum, diff
arr=[14,16,87,36,25,89,34]
M, N=1, 3
tmax=sorted(arr)[-M]
tmin=sorted(arr)[N-1]
s = tmax + tmin
d = tmax - tmin
print(f"{M}st maximum number = {tmax}")
print(f"{N}th minimum number = {tmin}")
print("Sum =", s)
print("Difference =", d)