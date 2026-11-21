import math

def solve():
    n = 100
    fact = math.factorial(n)
    digit_sum = sum(int(digit) for digit in str(fact))
    print(digit_sum)

if __name__ == "__main__":
    solve()
