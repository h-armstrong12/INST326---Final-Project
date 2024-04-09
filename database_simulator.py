# Simulated song database
songs_database = [
    {"title": "Song 1", "genre": "Pop", "emotion": "Happy"},
    {"title": "Song 2", "genre": "Rock", "emotion": "Energetic"},
    {"title": "Song 3", "genre": "Classical", "emotion": "Calm"},
    {"title": "Song 4", "genre": "Hip-Hop", "emotion": "Motivated"},
    {"title": "Song 5", "genre": "Jazz", "emotion": "Relaxed"},
    # Add more songs as needed
]

def fetch_songs_by_emotion(emotion):
    """
    Fetches songs from the simulated database based on the requested emotion.
    
    :param emotion: The emotion to filter songs by.
    :return: A list of songs matching the requested emotion.
    """
    return [song for song in songs_database if song["emotion"].lower() == emotion.lower()]
