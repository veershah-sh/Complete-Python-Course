# 4. Logical Operators

# Logical and
# Logical or
# Logical not

# Logical and

"""
Con1.  and   Con2.      Output
  T.          T.          T
  F           T.          F
  T           F.          F
  F.          F.          F


Con1.  or   Con2.      Output
  T.          T.          T
  F           T.          T
  T           F.          T
  F.          F.          F


Output = True
not(Output) = False
"""


num1 = 2
num2 = 20
num3 = 30
 

if ((num1>num2) and (num1>num3)):
    print("num1 is max")
else:
    print("num1 is not max")


if ((num1>num2) or (num1>num3)):
    print("num1 is max")
else:
    print("num1 is not max")

output = True

print(output)
print(not(output))
