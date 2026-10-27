def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
def is_palindrone(n):
    return n == reverse_number(n)
# a Test teh three functions
for i in (2026, 12321, 9875):
    print(f"{i}: digit sum = {digit_sum(i)}", 
          f"{i}: reversed = {reverse_number(i)}",
          f"{i}: palifrone = {is_palindrone(i)}")

# b Count palindromes from 10 to 999
count = 0
for i in range(10, 1000):
    if is_palindrone(i):
        count += 1
print("Palindromes from 10 to 999:", count)
