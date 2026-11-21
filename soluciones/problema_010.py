def solve():
    limit = 2000000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit, start):
                sieve[i] = False
                
    prime_sum = sum(i for i, is_prime in enumerate(sieve) if is_prime)
    print(prime_sum)

if __name__ == "__main__":
    solve()
