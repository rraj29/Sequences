panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "4,566,4523,8895,445,5656,55,4226,45"
print(numbers.split(","))

#   **JOIN will create a STRING from a list. SPLIT will create a LIST from a string.

#values = "".join(char if char not in separators else " " for numbers in numbers).split()
generated_list = ['9',' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7',
                  ]
values = "".join(generated_list)
print(values)
values_list = values.split()
print(values_list)

item_list_int = []
for item in values_list:
    item_list_int.append(int(item))
print(item_list_int)

for index in range(len(values_list)):
    values_list[index]= int(values_list[index])
print(values_list)