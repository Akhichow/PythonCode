vowels = set(["a", "e", "i", "o", "u"])

print("Please enter a statement")
sampleText = input()

finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)

# [' ', 'I', 'c', 'd', 'm', 'n', 'r', 's']

# My solution -

# finalList = []
#
# while True:
#     print("Please enter a statement")
#     text = input()
#
#     for alphabet in text:
#         if (alphabet not in vowels) and (alphabet != " "):
#             finalList.append(alphabet)
#
#     print(sorted(finalList))
#     print()
#     break

# ['I', 'c', 'c', 'd', 'd', 'm', 'n', 'r', 's']
