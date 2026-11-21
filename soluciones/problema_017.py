def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 1000:
        return "onethousand"
    
    words = ""
    
    hundreds_digit = n // 100
    remainder = n % 100
    
    if hundreds_digit > 0:
        words += ones[hundreds_digit] + "hundred"
        if remainder > 0:
            words += "and"
            
    if remainder >= 10 and remainder < 20:
        words += teens[remainder - 10]
    else:
        tens_digit = remainder // 10
        ones_digit = remainder % 10
        if tens_digit > 0:
            words += tens[tens_digit]
        if ones_digit > 0:
            words += ones[ones_digit]
            
    return words

def solve():
    total_letters = 0
    for i in range(1, 1001):
        total_letters += len(number_to_words(i))
    return total_letters

print(solve())
