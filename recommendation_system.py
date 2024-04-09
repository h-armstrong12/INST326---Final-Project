from database_simulator import fetch_songs_by_emotion

def recommend_songs(user_emotion):
    """
    Recommends songs based on the user's requested emotion.
    
    :param user_emotion: The emotion input by the user.
    :return: None
    """
    recommended_songs = fetch_songs_by_emotion(user_emotion)
    
    if recommended_songs:
        print(f"Songs that might make you feel {user_emotion}:")
        for song in recommended_songs:
            print(f"- {song['title']} (Genre: {song['genre']})")
    else:
        print("Sorry, we couldn't find any songs that match your mood. Try a different emotion.")

if __name__ == "__main__":
    user_emotion = input("How do you want to feel today? ")
    recommend_songs(user_emotion)
