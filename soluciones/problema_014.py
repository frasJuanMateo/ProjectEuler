def solve():
    limit = 1000000
    memo = {1: 1}

    def get_length(n):
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            res = 1 + get_length(n // 2)
        else:
            res = 1 + get_length(3 * n + 1)
        memo[n] = res
        return res

    max_len = 0
    best_n = 0

    for i in range(1, limit):
        length = get_length(i)
        if length > max_len:
            max_len = length
            best_n = i

    print(best_n)

if __name__ == "__main__":
    solve()
