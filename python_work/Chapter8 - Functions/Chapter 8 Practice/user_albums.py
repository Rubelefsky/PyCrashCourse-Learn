# page 142
# 8.8 user albums
def make_album(artist_name, album_name, number_of_songs=None):
    """Function should take in an artist name and album title
    and return a dictionary containing these two pieces of info
    """
    album_info = {'artist': artist_name.title(), 
                  'title': album_name.title()
                  }
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    return album_info

artist_prompt = "\nWhat artist are you thinking of? "
album_prompt = f"\nWhat is your favorite album? "

print("Enter 'q' at any time to stop.")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break

    title = input(album_prompt)
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
    
    print("\nThanks for responding!")
