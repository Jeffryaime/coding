def make_album(artist_name, album_title, number_of_song=None):
    """Return a dictionary with the album information"""
    
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_song:
        album['number_of_song'] = number_of_song
    return album

while True:
    print('\nPlease enter your album information:')
    print('(Please enter q if you want to quit)')

    name = input("Who is your album's artist ")
    if name == 'q':
        break

    response = input("What is your album's title ")
    if response == 'q':
         break

    print('\n---Results---')
    print(f"The album's artist is {name}, and the album's title is {response}.")
