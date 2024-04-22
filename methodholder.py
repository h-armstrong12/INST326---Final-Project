#Will hold the methods that the program will rely on.

import time

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
    

def desiredlist(username):
    """
    Docstring
    
    """
    print("""Here's a list of genre's to chose from:
          Pop, Country, Rock, Instrumental, R&B, Soul, HipHop""") #will be updated later
    musicprefer = input("Enter what genre of music you would like to listen to: ") 
    #musicprefer: users will input the genre they would like to listen to (must be exactly as spelled)
    #unit test: make sure that the name of the genre(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again


    print("""Here are some common experiences/feelings felt through these songs: (list of emotions/feelings)""")
    emotionprefer = input("Within the genre(s) selected, what are you in the mood for?")
    #emotionprefer: users will input the emotion they want to eperience (must be exactly as spelled)
    #unit test: make sure that the name of the emotion(s)\desired experiences(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again

    # a list of songs that fit these descriptions (genre/experience) will be presented to the user.
    print("Here is your selection of music " + username)


    
def recommendation():
    """
    Docstring
    
    """
    #unit test: makes sure that the tracks match what the user wants.
    pass

def altertracks():
    """
    Docstring
    
    """
    #unit test: there will be a list of experiences that the user can change the track depending on their own toughts and ideas
    # but those changes will have to match the list and rules that the program is coded with, if so then the user will be 
    #asked to input changes that are expected and accepted by the program or can simply just quit.
    pass


def randomize():
    """
    Docstring
    
    """
    #unit test: test to make sure there is 10 random tracks from the list presented to the user.
    pass


    
        