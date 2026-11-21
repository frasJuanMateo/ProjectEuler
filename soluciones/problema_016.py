def main():
    n = 2 ** 1000
    digit_sum = sum(int(digit) for digit in str(n))
    print(digit_sum)

if __name__ == "__main__":
    main()
