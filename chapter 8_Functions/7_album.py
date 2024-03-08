def make_album(artist_name, album_title, number_of_song=None):
    """Return a dictionary with the album information"""
    
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_song:
        album['number_of_song'] = number_of_song
    return album

album_info = make_album('usher', 'confession')
print(album_info)
album_info_2 = make_album('michael jackson', 'thriller')
print(album_info_2)
album_info_3 = make_album('medjy', 'rebecca')
print(album_info_3)
album_info_4 = make_album('akon','konvict', 11)
print(album_info_4)