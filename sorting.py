pangram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3,6.7,67.4,78.3,0]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
print()
#       ** The SORTED METHOD creates a different list.
#       ** we can assign the SORTED list to another variable in SORTED METHOD as shown above.

numbers.sort()
#       **Here there is NO OTHER LIST CREATED. The list is just sorted in its own.
#       **therefore we can not assign it to another variable.
#       another_sorted_list = numbers.sort()     -> Output- NONE
#       Hence we don't get the required answer.
print(numbers)

missing_letters = sorted("The quick brown fox jumped over the lazy dog",
                         key = str.casefold)
#       **keuy = str.casefold will help us sort Case-INSENSITIVE'.
print(missing_letters)

names = ["Graham",
         "terry",
         "eric",
         "Terry",
         "michael",
         "John"
         ]
names.sort()
print(names)
print()
names.sort(key=str.casefold)
print(names)
