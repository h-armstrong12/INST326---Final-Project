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
    print("""Here you will be able to select whether you would like to have a list of songs recommened to you based on a series of questions (recommend), 
be able to choose your genre of music and be given a list of songs (select), 
be able to change the feelings associated with the songs in our textfile (alter), 
and get a randomized list of songs from our text file (randomize).""")
    time.sleep(2)
    print("\n")
    print("You have the choice to either: 'select', 'recommend', 'randomize' or 'alter'")
    print("Note: please type your choice correctly or the program will not recognize it.")
    print("\n")
    

def decision(selection, username):
    if str(selection) == "select":
        desiredlist(selection, username)
    elif str(selection) == "recommend":
        recommendation(selection, username)
    elif str(selection) == "randomize":
        randomize(selection, username)
    elif str(selection) == "alter":
        altertracks(selection, username)
    elif str(selection) == "exit".casefold():
        print("\n")
        print("You have chosen to quit the program, we hope you enjoyed using the Audio Library.")
        exit()

    else:
        print("We were unable to identify what you typed in. Why dont you try again?")
        
def cyclecontinue(selection, username):
    time.sleep(2)
    print("\n")
    print(f"Hi {username}, you have the choice to either quit the program ('EXIT'), or continue using the other features available.")
    selection = input("Would you like to use one of these features: 'recommend', 'randomize', 'alter', 'select': ")
    if selection.casefold == "EXIT".casefold:
        exit()
    else: 
        decision(selection, username)

def desiredlist(selection, username):
    """
    Docstring
    
    """
    #all this code allows users to access their desired list of songs based on genre of music
    recommendlist = []
    print("\n")
    print("""Here's a list of genre's to chose from:
          Pop, Country, Rock, Classical, R&B, Soul, HipHop""")
    print("\n")
    musicprefer = input("Enter what genre of music you would like to listen to: ")
    if musicprefer.casefold() == "Pop".casefold() or "Country".casefold() or "Rock".casefold() or "Classical".casefold() or "R&B".casefold() or "Soul".casefold() or "Hiphop".casefold():
        file = open("songlist.txt", "r")
        content = file.readlines()
        for i in content:
            discover = re.search(r"Genre: +([a-zA-Z]+)", i)
            if discover != None:
                capture = discover.group(1)
            if capture.casefold() == musicprefer.casefold():
                search = re.search(r"Title: +([a-zA-Z0-9]+.+, Genre:+ [a-zA-Z]+, [a-zA-Z]+: [a-zA-Z]+)", i)
                if search != None:
                    trial = search.group(1)
                    recommendlist.append(trial)
        print(recommendlist)
        print(f"Here is your selection of music, {username} we hope you enjoy!")
        print("\n")
        emotionprefer = input("Would you like to search for songs in this list that are associated with a certain emotion (yes/no): ")
        print("\n")
        if emotionprefer.lower() == "yes":
            content = []
            #content = recommendlist
            #desiredemotionlist = recommendlist
            print("""List of emotions throughout the list: 
            "Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Stressed",
            "Hopeful", "Love", "Angry", "Bored", "Confident", "Curious", "Fear")""")
            print("\n")
            desiredemotion = input("What are you in the mood for?: ")
            print("\n")
            #desiredemotion
            #file
            
            for x in recommendlist:
                matchemotion = re.search(r"Emotion: +([a-zA-Z]+)", x)
                #if matchemotion.group(1) != None:
                    #desiredemotionlist[x] = content[x]
                if matchemotion.group(1) == desiredemotion:
                    content.append(x)
                    #tracksemotion = re.search(r"Title: +([a-zA-Z0-9]+.+), Genre:", x)
                # else:
                #     if tracksemotion != None:
                #         desiredsongemotion = tracksemotion.group(1)
                #         desiredemotionlist.append(desiredsongemotion)
            print(content)
            if len(content) == 0:
                print(f"Sorry {username}, looks like there's no songs here which fit that description.")
        if emotionprefer.lower() == "no":
            quit() #code something in that will take the user back to the start.
    file.close()
    #offer users the chance to do over.
    cyclecontinue(selection, username)
    #musicprefer: users will input the genre they would like to listen to (must be exactly as spelled)
    #unit test: make sure that the name of the genre(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again


    #print("""Here are some common experiences/feelings felt through these songs: (list of emotions/feelings)""")
    #emotionprefer = input("Within the genre(s) selected, what are you in the mood for?")
    #emotionprefer: users will input the emotion they want to eperience (must be exactly as spelled)
    #unit test: make sure that the name of the emotion(s)\desired experiences(s) are spelled correctly, or the program wont understand. 
    #will ask user to input it again

    # a list of songs that fit these descriptions (genre/experience) will be presented to the user.


    
def recommendation(username, selection):
    """
    Docstring
    
    """
    print("Hello there!")
    time.sleep(1)
    emotion_select = input("""How/What are you feeling? (select 1): 
    "Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Stressed",
    "Hopeful", "Love", "Angry", "Bored", "Confident", "Curious", "Fear"
          """)
    realrecommendlist = []
    emotionlist = ["happy", "sad", "energized", "calm", "motivated", "lonely", "stressed","hopeful", "love", "angry", "bored", "confident", "curious", "fear"]
    if emotion_select.casefold() in emotionlist:
        #print("good job")
        textfile = open("songlist.txt", "r")
        
        recommendcontent = textfile.readlines()
        for i in recommendcontent:
            findemotion = re.search(r"Emotion: ([a-zA-Z]+)", i)
            if findemotion != None:
                newwork = findemotion.group(1)
            if newwork.casefold() == emotion_select.casefold():
                secondsearch = re.search(r"(^.*)", i)
                if secondsearch != None:
                    newtrial = secondsearch.group(1)
                realrecommendlist.append(newtrial)
        print(realrecommendlist)
    else:
        print("Did you mean to write something else? Why don't you try again:")
    
    

    
    #unit test: makes sure that the tracks match what the user wants.
    pass

def altertracks(username, selection):
    """
    Interactively allows a user to update the emotional tag associated with a track.
    Validates against a predefined list of acceptable emotions.
    
    Parameters:
    username (str): The name of the user.
    
    Returns:
    None: Directly outputs results and prompts user for additional changes.
    """
   
    print(f"Hello {username}, ready to update the emotional tags of your tracks.")
    valid_emotions = ["happy", "sad", "energized", "calm", "motivated", "lonely", "stressed","hopeful", "love", "angry", "bored", "confident", "curious", "fear"]
    track_name = input("Enter the track number to modify: ")
    file = open("songlist.txt", "r")
    content = file.readlines()
    for i in content:
        tracknumber = re.search(r"([0-9]+):", i)
        if tracknumber != None:
            capture = tracknumber.group(1)
        if capture == track_name:
            wholetrack = re.search(r"(^.*)", i)
            with open("altersonglist.txt", "a+") as writefile:
                #print(wholetrack.group(1))
                writefile.write(wholetrack.group(1) + "\n") 
                        
    new_emotion = input(f"Enter new emotion from: {', '.join(valid_emotions)}: ")
    if new_emotion in valid_emotions:
        print(f"Updated '{track_name}' with new emotion: {new_emotion}.")   
        with open("altersonglist.txt", "r") as file:
            writefile = file.readlines()
            
        for i, line in reversed(list(enumerate(writefile))):  
            if isinstance (line, str):  
                emotion = re.search(r"Emotion: ([a-zA-Z]+)", line)
                if emotion != None:
                    replaceemotion = emotion.group(1)
                    emotion_str = str(new_emotion).casefold()
                    writefile[i] = (re.sub(replaceemotion, emotion_str, line))
                    break
        with open("altersonglist.txt", "w") as file:
            file.writelines(writefile)   
    
    else:
        print(f"Invalid emotion. Available emotions are: {', '.join(valid_emotions)}.")
    
    if input("Modify another track? (yes/no): ").lower() == 'yes':
        altertracks(username, selection)
    else:
        print("Exiting track modification.")


def randomize(selection, username):
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
    #offer users the chance to do over.
    cyclecontinue(selection, username)

    #unit test: test to make sure there is 10 random tracks from the list presented to the user.
        
