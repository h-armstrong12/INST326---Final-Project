"""
Inst 326 (Ruka Ayele, Hannah Armstrong)
Final Project - Emotion/Genre-Based Music Library Management and Recommendation System

Goal: We plan on developing a library management system that categorizes songs not only by
traditional metrics (e.g., genre) but also by the emotions or experiences they evoke (e.g.,
happiness, motivation, relaxation) in people.

"""


#username input
def username():
    """
    Docstring
    
    """
    username = input("Enter username: ")

    #unit test: make sure that the username is not empty, the user should input a name


#will ask users if they want to just look for music, find their musical tastes through a small quiz,
#alter some of the descriptive terms for each song (if they see fit) or generate a random playlist.

def desiredlist():
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