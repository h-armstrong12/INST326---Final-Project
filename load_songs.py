def load_songs_from_file(filepath="songlist.txt"):
    songs = []
    with open(filepath, 'r') as file:
        for line in file:
            # Skip empty lines or comments
            if line.strip() == "" or line.startswith('#'):
                continue
            parts = line.strip().split(', ')
            song_info = {part.split(': ')[0]: part.split(': ')[1] for part in parts}
            songs.append(song_info)
    return songs

# Example usage
songs = load_songs_from_file()
for song in songs:
    print(song)
