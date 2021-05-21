welcome = "Welcome to my nightmare", "Alice Cooper", 1973
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mahyem", "Emilda May", 2011
metallica = "Ride the lightning", "Metalliva", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
#   *TUPLES ARE GOOD TO STORE THE DATA WHICH WE WANT TO PROTECT AND NOT CHANGE.
#   metallica[0] = "Master of Puppets"  -> it will give an ERROR, if we try to modify the contents of a tuple.
metallica2 = list(metallica)
metallica2[0] = "Master of Puppets"
print(metallica2)

table = "Coffee Table", 200, 100, 75, 345.50
print(table[1]*table[2])
name, length, breadth, height, price = table
print(length*breadth)