# 1. Count primes and composites
n=[4,54,29,71,59,98,23]
is_prime=lambda x:x>1 and all(x%i for i in range(2,int(x**0.5)+1))
p=sum(is_prime(i) for i in n)
c=sum(i>1 and not is_prime(i) for i in n)
print("Prime numbers =", p)
print("Composite numbers =", c)