# a


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# b
print("Primes below 50:", end=" ")
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")
print()

count = 0
for i in range(2, 100):
    if is_prime(n):
        count += 1

print("Number of primes below 100:", count)


# c
def goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)
    return None


for i in (4, 6, 8):
    p, q = goldbach(i)
    print(f"{i} = {p} + {q}")
print("...")
p, q = goldbach(30)
print(f"30 = {p} + {q}")

# d
holds = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        holds = False
        break
print("Goldbach holds for every even number from 4 to 10000: ", holds)
