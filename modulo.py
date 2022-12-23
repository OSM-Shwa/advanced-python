# MODULAR ARITHMETIC

# Arithmetic on a group of integers that "wrap around" when the maximum value is reached
# Think of a 12-hour clock;
# - 2 o'clock + 5 hours = 7 o'clock
# - 7 o'clock + 6 hours = 1 o'clock
# 13 mod 12 = 1


# How mod is calculated:
# r = a % n
# r = a - (n * floor(a/n))

# Example:
# r = 13 % 12
# r = 13 - (12 * floor(13/12))
# r = 13 - (12 * floor(1.08333))
# r = 13 - (12 * 1)
# r = 1

# Example:
# r = 8 % -3
# r = 8 - (-3 * floor(8/-3))
# r = 8 - (-3 * floor(-2.6666))
# r = 8 - (-3 * -3)
# r = -1

print(8%-3)