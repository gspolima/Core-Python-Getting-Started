from exceptional import convert


nice_numbers = convert('four two six nine'.split())
print(nice_numbers)

not_so_nice_numbers = convert('one bazillion'.split())
print(not_so_nice_numbers)

inexistent_number = convert(1997)
print(inexistent_number)