# Bitwise Operators
# Python provides 6 bitwise operators:
# 1) << : Left shift operator
# 2) >> : Right shift operator
# 3) ~ : Ones Complement operator
# 4) & : Bitwise And
# 5) | : Bitwise Or
# 6) ^ : Bitwise Xor

# These operators act on the binary digits (bits) of integers.

# Left shift operator: <<
# It is a binary bitwise operator.
# It acts on the value of the LHS operand. Its binary digits are shifted leftwards by places specifed by the RHS operand.
# There is no data loss at MSB.
# In Python, integers have expanding allocation, so the size of the variable will expand to accomodate the extra bits.
# Blanks are created at the LSB and are autofilled with zeros.
x = 12
y = 3
z = x << y
print(x, "<<", y, "=", z)

# Right shift operator: >>
# It is a binary bitwise operator.
# It acts on the value of the LHS operand. Its binary digits are shifted righwards by places specifed by the RHS operand.
# There is  loss of data at LSB.
# Blanks are created at the MSB and are autofilled with zeros.

x = 12
y = 3
z = x >> y
print(x, ">>", y, "=", z)

# & : Bitwise And
# It is a binary bitwise operator.
# It performs AND MASKING on the bits of the 2 operands.
# AND MASKING rules:
# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

x = 19
y = 5
z = x & y
print(x, "&", y, "=", z)

# | : Bitwise Or
# It is a binary bitwise operator.
# It performs OR MASKING on the bits of the 2 operands.
# OR MASKING rules:
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0

x = 19
y = 5
z = x | y
print(x, "|", y, "=", z)
