from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your album(invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
    # #for index, title, artist, year, songs in enumerate(albums):
    # # like above Removing the bracket will give error bcoz ENUMERATE returns ONLY 2 values, NOT 5
         print("{}: {}".format(index+1, title))

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print("{}. {}".format(index+1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")
    for index,(track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index+1,song))
    song_choice = int(input())
    if 1<= song_choice <= len(songs_list):
        title = songs_list[song_choice-1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("="*98)
    #else:
        #break


