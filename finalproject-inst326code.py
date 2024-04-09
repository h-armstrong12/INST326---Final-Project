"""
Inst 326 (Ruka Ayele, Hannah Armstrong)
Final Project - Emotion/Genre-Based Music Library Management and Recommendation System

Goal: We plan on developing a library management system that categorizes songs not only by
traditional metrics (e.g., genre) but also by the emotions or experiences they evoke (e.g.,
happiness, motivation, relaxation) in people.

"""


#username input
def username():
    username = input("Enter username: ")


#will ask users if they want to feel 

def desiredlist():
    print("""Here's a list of genre's to chose from:
          Pop, Country, Rock, Instrumental, R&B, Soul, HipHop""") #will be updated later
    musicprefer = input("Enter what genre of music you would like to listen to: ") 
    #musicprefer: users will input the genre they would like to listen to (must be exactly as spelled)
    print("""Here are some common experiences/feelings felt through these songs: (list of emotions/feelings)""")
    emotionprefer = input("Within the genre(s) selected, what are you in the mood for?")
    #emotionprefer: users will input the emotion they want to eperience (must be exactly as spelled)

    # a list of songs that fit these descriptions (genre/experience) will be presented to the user.
    print("Here is your selection of music " + username)


def recommendation():
    pass



def personalize():
    pass