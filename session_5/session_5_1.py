a = {1,2,3,4,5,6}
b = {5,6,7,8,9,2}

# intersection
anb = a.intersection(b)
# print(anb)

# a.intersection_update(b)
# print(a)


# difference
a_b = a.difference(b)
# print(a_b)

b_a = b.difference(a)
# print(b_a)

# symmetric diference
a__b = a.symmetric_difference(b)
print(a__b)


# union
aub = a.union(b)
# print(aub)

# isdisjoint
# if no elements of set(a) and set(b) are common than the set is disjoint set.
a_dis_b = a.isdisjoint(b)
print(a_dis_b)

# issubset
# if all the elements of set(a) is in set(b) than set(a) is subset of set(b)
a_sub_b = a.issubset(b)
print(a_sub_b)

# issuperset
# if all the elements of set(b) is in set(a) than a is superset of b
a_sup_b = a.issuperset(b)
print(a_sup_b)