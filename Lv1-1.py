nums = []
while True:
    n = int(input("Enter number (-1 to stop): "))
    if n == -1:
        break
    nums.append(n)

pos = [x for x in nums if x > 0]
neg = [x for x in nums if x < 0]

print("Avg positive:", sum(pos)/len(pos))
print("Avg negative:", sum(neg)/len(neg))
