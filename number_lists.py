empty_list =[]
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
# numbers = even + odd
# print(numbers)
#
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = sorted("423569871")
# print(digits)
#
# digits_as_strings = list('423569871')
# print(digits_as_strings)
#
# #       ***These are the ways to copy the list to another list.
# #more_numbers = list(numbers)
# #more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)      #this shows that they are different
# print(numbers == more_numbers)      #this shows that they are equal i.e. same values at same places



# even.extend(odd)
# print(even)
#
# even.sort()
# print(even)
# another_even = even
# print(another_even)
# #   **Note that .SORT method just rearranges that list. It does NOT create a new list.
# #   **this can be important if our list is of size GBs.
# even.sort(reverse=True)
# print(even)
# print(another_even)
# print(min(even))
# print(min(odd))
# print(max(even))
# print(max(odd))
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("Mississipi".count("iss"))
