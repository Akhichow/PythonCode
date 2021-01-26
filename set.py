#   Two ways to create a set

#   First method - direct
#
# farm_animals = {"cow", "hen", "goat"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# #   Using set keyword
#
# wild_animals = set(["tiger", "lion", "elephant", "giraffe"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# f = sorted(farm_animals)
# w = sorted(wild_animals)
#
# print(f)
# print(w)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = set([4, 6, 9, 16, 25])
# print(squares_tuple)
# print(len(squares_tuple))
#
# print(even.union(squares_tuple))
# print(len(even.union(squares_tuple)))
#
# # print(even.intersection(squares_tuple))
# # print(len(even.intersection(squares_tuple)))
#
# print(even & squares_tuple)
# print(len(even & squares_tuple))

# even = set(range(0, 40, 2))
# print(even)
# squares = set([4, 6, 9, 16, 25])
# print(squares)

# print("even minus squares_tuple")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))

# print("Even difference_update Squares")
# even.difference_update(squares)
# print(sorted(even))

# print("Squares difference_update Even")
# squares.difference_update(even)
# print(squares)

# print("Even symmetric_update Squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("Squares symmetric_update even")
# print(sorted(squares.symmetric_difference(even)))

# even.discard(8)
# print(even)
#
# try:
#     even.remove(8)
# except KeyError:
#     print("Item 8 is not a member of the set")

# even = set(range(0, 40, 2))
# print(even)
# squares = set([4, 6, 16])
# print(squares)
#
# if squares.issubset(even):
#     print("Squares is a subset of even")
#
# if even.issuperset(squares):
#     print("Even is a superset of squares")
#
# A = set([2, 4, 6])
# B = set([2, 3, 4, 5, 6])
#
# if A.issubset(B):
#     print("A is a subset of B")
#
# if B.issuperset(A):
#     print("B is a superset of A")

even = frozenset(range(0, 100, 2))

print(even)
