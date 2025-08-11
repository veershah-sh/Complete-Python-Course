# 6. Identity Operators

# is
# is not

a = [1,2,3]
b = a
c = [4,5,6]

print(a is b)
print(a is  c)

print(a is not b)
print(a is not c)

p1 = "abc"
p2 = "def"
p3 = "abc"

print(p1 is p3)
print(p1 is p2)

# interview question
# == -> is
# != -> is not

print(p1 == p3)
print(p1 is p3)