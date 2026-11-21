def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def solve():
    # 1 Jan 1900 was a Monday.
    # Let's count days starting from 1 Jan 1900.
    # Monday = 0, Tuesday = 1, ..., Sunday = 6
    
    current_day_of_week = 0  # 1 Jan 1900 is Monday (0)
    
    # First, advance to 1 Jan 1901
    current_day_of_week = (current_day_of_week + days_in_month(1900, 1)) % 7
    # For months 2 to 12 of 1900
    for m in range(2, 13):
        current_day_of_week = (current_day_of_week + days_in_month(1900, m)) % 7
        
    # Now current_day_of_week is the day of the week for 1 Jan 1901
    sunday_count = 0
    
    # Iterate through the 20th century: 1 Jan 1901 to 31 Dec 2000
    for year in range(1901, 2001):
        for month in range(1, 13):
            if current_day_of_week == 6:  # Sunday
                sunday_count += 1
            current_day_of_week = (current_day_of_week + days_in_month(year, month)) % 7
            
    print(sunday_count)

if __name__ == "__main__":
    solve()
