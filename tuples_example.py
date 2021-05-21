albums = [("Welcome to my nightmare", "Alice Cooper", 1973),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mahyem", "Emilda May", 2011),
          ("Ride the lightning", "Metalliva", 1984),
          ]

print(len(albums))

#Better method. Preferable
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print("-"*45)

for album in albums:
    name,artist,year = album
    print("Album: {}, Artist: {}, Year: {}"
        .format(name, artist, year))