shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = shopping_list
#the above assignment is effectively
# a = shopping_list
# b = shopping_list
# c = shopping_list
# d = shopping_list
#THERE IS ONLY ONE LIST, ONLY THERE ARE MULTIPLE NAMES ATTACHED TO IT.

print(a)
print("adding cake")
b.append("cake")
#CAKE is appended to each and every name of the list.
print(d)