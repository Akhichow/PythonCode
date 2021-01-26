shopping_list = ["apple", "spam", "milk", "pasta", "bread", "eggs"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)
