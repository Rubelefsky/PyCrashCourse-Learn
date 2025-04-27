# page 142 
# 8.7

def make_album(artist_name, album_name, number_of_songs=None):
    """Function should take in an artist name and album title
    and return a dictionary containing these two pieces of info
    """
    album_info = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    return album_info

album1 = make_album('lloyd banks', 'cold corner 2', number_of_songs=15)
print(album1)
album2 = make_album('the beatles', 'abbey road')
print(album2)
