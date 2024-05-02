#Will hold the methods that the program will rely on.

import time
import re
import random
#import emotions
#import songlist
def intro_username(username):
    """
    Docstring
    
    """
    print("Hello " + username + ", welcome to (insert program name). A Emotion/Genre-Based Music Library Management and Recommendation System.")
    time.sleep(1)
    print("\n")
    print("""Here you will be able to select whether you would like to have songs recommened to you based on a series of questions, 
be able to choose your genre of music and be given a list of recommendations, 
be able to alter/change the feelings/emtotions associated with tracks in our songlist, 
and get a randomized list of songs that will give you the chance to experiment.""")
    time.sleep(2)
    print("\n")
    print("You have the option to choose to either use the program to: 'select', 'recommend', 'randomize' or 'alter'  ")
    print("Note: please type your choice correctly or the program will not recognize it.")
    

def decision(selection, username):
    if str(selection) == "select":
        desiredlist(username)
    elif str(selection) == "recommend":
        recommendation(username)
    elif str(selection) == "randomize":
        randomize(username)
    elif str(selection) == "alter":
        altertracks(username)
    else:
        print("We were unable to identify what you typed it. Why dont you try again?")
        


def desiredlist(username):
    """
    Docstring
    
    """
    #all this code allows users to access their desired list of songs based on genre of music
    recommendlist = []
    print("""Here's a list of genre's to chose from:
          Pop, Country, Rock, Classical, R&B, Soul, HipHop""") #will be updated later
    musicprefer = input("Enter what genre of music you would like to listen to: ")
    if musicprefer.casefold() == "Pop".casefold() or "Country".casefold() or "Rock".casefold() or "Classical".casefold() or "R&B".casefold() or "Soul".casefold() or "Hiphop".casefold():
        file = open("songlist.txt", "r")
        content = file.readlines()
        for i in content:
            discover = re.search(r"Genre: +([a-zA-Z]+)", i)
            if discover != None:
                capture = discover.group(1)
            if capture.casefold() == musicprefer.casefold():
                search = re.search(r"Title: +([a-zA-Z0-9]+.+), Genre:", i)
                if search != None:
                    trial = search.group(1)
                    recommendlist.append(trial)
        print(recommendlist)
        print(f"Here is your selection of music, {username} we hope you enjoy!")

        emotionprefer = input("Would you like to search for specific emotions/feelings that is found in this selection of music? (yes/no): ")
        if emotionprefer.lower() == "yes":
            desiredemotionlist = []
            print("List of emotions throughout the list: (Happy), (Sad), (Energetic), (Calm) (...)")
            desiredemotion = input("What are you in the mood for?: ")
            file
            content
            for x in content:
                matchemotion = re.search(r"Emotion: +([a-zA-Z]+)", x)
                if matchemotion != None:
                    pairemotion = matchemotion.group(1)
                if pairemotion == desiredemotion:
                    tracksemotion = re.search(r"Title: +([a-zA-Z0-9]+.+), Genre:", x)
                    if tracksemotion != None:
                        desiredsongemotion = tracksemotion.group(1)
                        desiredemotionlist.append(desiredsongemotion)
            print(desiredemotionlist)
            if len(desiredemotionlist) == 0:
                print("Sorry Hannah, looks like there's no songs here which fit that description.")
        if emotionprefer.lower() == "no":
            quit() #code something in that will take the user back to the start.
        
    #musicprefer: users will input the genre they would like to listen to (must be exactly as spelled)
    #unit test: make sure that the name of the genre(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again


    #print("""Here are some common experiences/feelings felt through these songs: (list of emotions/feelings)""")
    #emotionprefer = input("Within the genre(s) selected, what are you in the mood for?")
    #emotionprefer: users will input the emotion they want to eperience (must be exactly as spelled)
    #unit test: make sure that the name of the emotion(s)\desired experiences(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again

    # a list of songs that fit these descriptions (genre/experience) will be presented to the user.


    
def recommendation(username):
    """
    Docstring
    
    """
    print("Hello there!")
    time.sleep(1)
    emotion_select = input("""How/What are you feeling? (select 1): 
"Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Stressed",
"Hopeful", "Love", "Angry", "Bored", "Confident", "Curious", "Fear"
          """)
    
    if emotion_select.lower() == "happy" or "sad" or "energized" or "calm" or "motivated" or "lonely" or "stressed" or "hopeful" or "love" or "angry" or "confident" or "curious" or "fear":
        print("good work so far")

    
    #unit test: makes sure that the tracks match what the user wants.
    pass

def altertracks(username):
    """
    Interactively allows a user to update the emotional tag associated with a track.
    Validates against a predefined list of acceptable emotions.
    
    Parameters:
    username (str): The name of the user.
    
    Returns:
    None: Directly outputs results and prompts user for additional changes.
    """
   
    print(f"Hello {username}, ready to update the emotional tags of your tracks.")
    valid_emotions = ["Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Joyful", "Stressed"]
    track_name = input("Enter the track name to modify: ")
    new_emotion = input(f"Enter new emotion from {', '.join(valid_emotions)}: ")
    
    if new_emotion in valid_emotions:
        print(f"Updated '{track_name}' with new emotion: {new_emotion}.")
    else:
        print(f"Invalid emotion. Available emotions are: {', '.join(valid_emotions)}.")
    
    if input("Modify another track? (yes/no): ").lower() == 'yes':
        altertracks(username)
    else:
        print("Exiting track modification.")


def randomize(username):
    """
    Docstring
    
    """
    print("Hello there!")
    print("Here is a randomized list of 10 songs from the songlist file.")
    file = open("songlist.txt", "r")
    content = file.read()
    listData = []
    listData = content.split("\n")
    #print(listData)
    print(random.sample(listData, 10))

    #unit test: test to make sure there is 10 random tracks from the list presented to the user.
        
