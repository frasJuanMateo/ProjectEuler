def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

def solve():
    n = 1
    triangle = 0
    while True:
        triangle += n
        if count_divisors(triangle) > 500:
            return triangle
        n += 1

print(solve())
