flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]
#
# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)       # | The JOIN is a method of STRINGS.
#   It creates a string from the iterable, that it is called on.
print(output)

print(", ".join(flowers))
#   *** ALL THE ITEMS IN THE ITERABLE MUST BE STRINGS FOR IT TO WORK.
#   If we add any integer to the above list, the program will crash with error. 