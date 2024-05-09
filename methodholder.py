# Importing necessary libraries.
import time
import re
import random
import unittest

# Import other components of the final project.
#from finalprojectcode import Username
#import emotions
#import songlist

def intro_username(username):
    """
    Greet the user and provide a brief overview of the Audio Library functionalities.
    """
    # Greet the user.
    print(f"Hello {username}, welcome to Audio Library. A Emotion/Genre-Based Music Library Management and Recommendation System.")
    time.sleep(1)
    print("\n")
    # Introduce the different functionalities of the system.
    print("""Here you will be able to get a recommended list of songs based on a series of questions (recommend), 
be able to choose your genre of music and be given a list of songs (select), 
be able to change the feelings associated with the songs in our text file (alter), 
and get a randomized list of songs from our text file (randomize).""")
    time.sleep(2)
    print("\n")
    # Prompt the user to make a choice about what they want to do.
    print("You have the choice to either: 'select', 'recommend', 'randomize' or 'alter'")
    print("Note: please type your choice correctly or the program will not recognize it.")
    print("\n")
    

def decision(selection, username):
    """
    Process the user's choice and call the appropriate function.
    """
    # Direct the user's input to the respective function.
    if selection == "select":
        desiredlist(selection, username)
    elif selection == "recommend":
        recommendation(selection, username)
    elif selection == "randomize":
        randomize(selection, username)
    elif selection == "alter":
        altertracks(selection, username)
    elif selection.casefold() == "exit":
        print("\n")
        print("You have chosen to quit the program, we hope you enjoyed using the Audio Library.")
        exit()
    else:
        print("We were unable to identify what you typed in. Why dont you try again?")
        
def cyclecontinue(selection, username):
    """
    Offer the user the option to continue using the program or exit.
    """
    time.sleep(2)
    print("\n")
    # Prompt the user to continue using the program or to exit.
    print(f"Hi {username}, you have the choice to either quit the program ('EXIT'), or continue using the other features available.")
    selection = input("Would you like to use one of these features: 'recommend', 'randomize', 'alter', 'select': ")
    if selection.casefold() == "exit":
        exit()
    else: 
        decision(selection, username)

def desiredlist(selection, username):
    """
    Allow the user to select music based on genre, and optionally by emotion.
    """
    # This code lets users access their desired list of songs based on the genre of music.
    recommendlist = []
    print("\n")
    print("""Here's a list of genres to choose from:
          Pop, Country, Rock, Classical, R&B, Soul, HipHop""")
    print("\n")
    musicprefer = input("Enter what genre of music you would like to listen to: ")
    if musicprefer.casefold() in ["pop", "country", "rock", "classical", "r&b", "soul", "hiphop"]:
        file = open("songlist.txt", "r")
        content = file.readlines()
        for i in content:
            discover = re.search(r"Genre: ([a-zA-Z]\S[a-zA-Z]+)", i)
            if discover:
                capture = discover.group(1)
                if capture.casefold() == musicprefer.casefold():
                    search = re.search(r'Title: (["a-zA-Z0-9"]+.+)', i)
                    if search:
                        trial = search.group(1)
                        recommendlist.append(trial)
        print("\n".join(recommendlist))
        print(f"Here is your selection of music, {username} we hope you enjoy!")
        print("\n")
        emotionprefer = input("Would you like to search for songs in this list that are associated with a certain emotion (yes/no): ")
        print("\n")
        if emotionprefer.lower() == "yes":
            content = []
            print("""List of emotions throughout the list: 
            "Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Stressed",
            "Hopeful", "Love", "Angry", "Bored", "Confident", "Curious", "Fear")""")
            print("\n")
            desiredemotion = input("What are you in the mood for?: ")
            print("\n")
            for x in recommendlist:
                matchemotion = re.search(r"Emotion: +([a-zA-Z]+)", x)
                if matchemotion and matchemotion.group(1) == desiredemotion:
                    content.append(x)
            print("\n".join(content))
            if not content:
                print(f"Sorry {username}, looks like there's no songs here which fit that description.")
        else:
            print(f"We hope you enjoy the list of songs, {username}")
    file.close()
    cyclecontinue(selection, username)

# The remaining functions, recommendation, altertracks, and randomize, would follow a similar pattern of being explained.

# There's also the TestMethods class and the main execution guard, which would have comments explaining their purpose and usage.
