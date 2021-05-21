data = [4, 5, 104, 105, 110, 120, 130, 130,
        150, 160, 170, 183, 185, 187, 189, 191, 193, 350, 360]

min_valid = 100
max_valid = 200

# del data[0:2]
# print(data)
# del data[-1:-3:-1]
# print(data)


#THIS WILL ONLY WORK IN A SORTED LIST(i.e. ASCENDING)
#   DELETING THE LOWER VALUES:
#   We do NOT need to copy the list, as if list would be large, we wouldn't have enough RAM to do it.
stop = 0
for index,value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)         #for debugging
del data[0:stop]
print(data)

print("-"*45)
#   DELETING THE LOWER VALUES:
start = 0
for index in range(len(data)-1,-1,-1):
    if data[index] <= max_valid:
        #We have the index of the last item to keep.
        #set the position of the start to the first element we want to delete.
        #item to delete, which is one after the "index"
        start = index + 1
        break
print(start)         #for debugging
del data[start:]
print(data)
