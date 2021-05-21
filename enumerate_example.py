for index, character in enumerate("abcdefg"):
    print(index, character)

for t in enumerate("sdfghjk"):
    print(t)

#   ****VERY IMPORTANT -> CODE FOR UNPACKING A TUPLE.
#       It effectively does what the first code did for us.
for t in enumerate("sdfghjk"):
    index, character = t
    print(index, character)