# page 142
# 8.8 user albums
def make_album(artist_name, album_name, number_of_songs=None):
    """Function should take in an artist name and album title
    and return a dictionary containing these two pieces of info
    """
    album_info = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    return album_info

    