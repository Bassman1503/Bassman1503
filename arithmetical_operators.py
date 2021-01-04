a= 14
b= 3

# Classical division operator.
#
trueDivision= a/b
print(trueDivision)

# Division operator which rounds the result value towards minus infinity.
#
integerDivision= a//b
print(integerDivision)

# Remainder of the division operation.
#
remainder= a % b
print(remainder)

# Truncation of the decimal part of the result of the division.
# Truncation rounds towards 0.
#
print(int(a/b))

# Use underscores within number literal strings to make big numbers more readable.
#
anInt= 1_000_000_000
print(anInt)