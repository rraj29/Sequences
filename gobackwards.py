data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_val = 100
max_val = 200
# Note that this list is NOT SORTED, it needs to be done differently.


# for index in range(len(data)-1,-1,-1):
#     if data[index]< min_val or data[index]> max_val:
#         print(index, data)
#         del data[index]

top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    if value< min_val or value> max_val:
        del data[top_index- index]
        print(top_index- index,value)

print(data)