#Will hold the methods that the program will rely on.

import time
import re
import random
import unittest

#from finalprojectcode import Username

#import emotions
#import songlist

def intro_username(username):
    """
    Docstring
    
    """
    print("Hello " + username + ", welcome to Audio Library. A Emotion/Genre-Based Music Library Management and Recommendation System.")
    time.sleep(1)
    print("\n")
    print("""Here you will be able to get a recommened list of songs based on a series of questions (recommend), 
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
    print("You have the choice to either quit the program ('EXIT'), or continue using the other features available.")
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
    if musicprefer.casefold() == "pop".casefold() or "country".casefold() or "rock".casefold() or "classical".casefold() or "r&b".casefold() or "soul".casefold() or "hiphop".casefold():
        file = open("songlist.txt", "r")
        content = file.readlines()
        for i in content:
            discover = re.search(r"Genre: ([a-zA-Z]\S[a-zA-Z]+)", i)
            if discover != None:
                capture = discover.group(1)
            if capture.casefold() == musicprefer.casefold():
                search = re.search(r'Title: (["a-zA-Z0-9"]+.+)', i)
                if search != None:
                    trial = search.group(1)
                    recommendlist.append(trial)
        print("\n".join(recommendlist))
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
            print("\n".join(content))
            if len(content) == 0:
                print(f"Sorry {username}, looks like there's no songs here which fit that description.")
        if emotionprefer.lower() != "yes":
            print(f"We hope you enjoy the list of songs, {username}") #code something in that will take the user back to the start.

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


    
def recommendation(selection, username):
    """
    Docstring
    
    """
    print("Hello there!")
    time.sleep(1)
    emotion_select = input("""How/What are you feeling? (select 1): 
    "Happy", "Sad", "Energized", "Calm", "Motivated", "Lonely", "Stressed",
    "Hopeful", "Love", "Angry", "Bored", "Confident", "Curious", "Fear"
          """)
    print("\n")
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
        print("\n".join(realrecommendlist))
        print("\n")
    
    else:
        print("Did you mean to write something else? Why don't you try again:")
        recommendation(selection, username)
    
    textfile.close()
    
    theme_option = input("Would you like to listen to songs with specific lyrical themes: (yes/no) ")
    print("\n")
    secondlist = []
    thirdlist = []
    if theme_option == "yes".casefold():
        
        print("Here's a list of themes: Romance, Empowerment, Peace, Heartbreak, Optimism ")
        theme_select = input("Select a theme you would be interested in: ")
        print("\n")
        if theme_select == "romance".casefold() and emotion_select != "love".casefold():
            textfile = open("songlist.txt", "r")
            recommendcontent = textfile.readlines()
            for i in recommendcontent:
                secondfindemotion = re.search(r"Emotion: (Love)", i)
                if secondfindemotion != None:
                    secondemotion = secondfindemotion.group(1)
                    if secondemotion.casefold() == "Love".casefold():
                        tracksearch = re.search(r"(^.*)", i)
                        if tracksearch != None:
                            songtrial = tracksearch.group(1)
                        secondlist.append(songtrial)       
            print("\n".join(secondlist))
            textfile.close()

        if theme_select == "empowerment".casefold() and emotion_select != "motivated".casefold():
            
            textfile = open("songlist.txt", "r")
            recommendcontent = textfile.readlines()
            for i in recommendcontent:
                thirdfindemotion = re.search(r"Emotion: (Motivated)", i)
                if thirdfindemotion != None:
                    thirdemotion = thirdfindemotion.group(1)
                    if thirdemotion.casefold() == "Motivated".casefold():
                        empowersongsearch = re.search(r"(^.*)", i)
                        if empowersongsearch != None:
                            songtrial = empowersongsearch.group(1)
                        thirdlist.append(songtrial)       
            print("\n".join(thirdlist))
            textfile.close()

        if theme_select == "peace".casefold() and emotion_select != "calm".casefold():
            
            textfile = open("songlist.txt", "r")
            recommendcontent = textfile.readlines()
            for i in recommendcontent:
                thirdfindemotion = re.search(r"Emotion: (Calm)", i)
                if thirdfindemotion != None:
                    thirdemotion = thirdfindemotion.group(1)
                    if thirdemotion.casefold() == "Calm".casefold():
                        empowersongsearch = re.search(r"(^.*)", i)
                        if empowersongsearch != None:
                            songtrial = empowersongsearch.group(1)
                        thirdlist.append(songtrial)       
            print("\n".join(thirdlist))
            textfile.close()

        if theme_select == "heartbreak".casefold() and emotion_select != "sad".casefold():
            
            textfile = open("songlist.txt", "r")
            recommendcontent = textfile.readlines()
            for i in recommendcontent:
                thirdfindemotion = re.search(r"Emotion: (Sad)", i)
                if thirdfindemotion != None:
                    thirdemotion = thirdfindemotion.group(1)
                    if thirdemotion.casefold() == "Sad".casefold():
                        empowersongsearch = re.search(r"(^.*)", i)
                        if empowersongsearch != None:
                            songtrial = empowersongsearch.group(1)
                        thirdlist.append(songtrial)       
            print("\n".join(thirdlist))
            textfile.close()
        
        if theme_select == "optimism".casefold() and emotion_select != "hopeful".casefold():
            
            textfile = open("songlist.txt", "r")
            recommendcontent = textfile.readlines()
            for i in recommendcontent:
                thirdfindemotion = re.search(r"Emotion: (Hopeful)", i)
                if thirdfindemotion != None:
                    thirdemotion = thirdfindemotion.group(1)
                    if thirdemotion.casefold() == "Hopeful".casefold():
                        empowersongsearch = re.search(r"(^.*)", i)
                        if empowersongsearch != None:
                            songtrial = empowersongsearch.group(1)
                        thirdlist.append(songtrial)       
            print("\n".join(thirdlist))
            textfile.close()

        else:
            print("Looks like you already have these tracks in your first list.")
            


    thirdquestion = input("Are you in the mood for music that is fast-paced or slow: ")
    print("\n")
    if thirdquestion == "fast-paced".casefold() or "fast".casefold() or "fastpaced".casefold() and thirdquestion != "energized".casefold():
        textfile = open("songlist.txt", "r")
        recommendcontent = textfile.readlines()
        for i in recommendcontent:
            thirdfindemotion = re.search(r"Emotion: (Energized)", i)
            if thirdfindemotion != None:
                thirdemotion = thirdfindemotion.group(1)
                if thirdemotion.casefold() == "Energized".casefold():
                    empowersongsearch = re.search(r"(^.*)", i)
                    if empowersongsearch != None:
                        songtrial = empowersongsearch.group(1)
                    thirdlist.append(songtrial)       
        print("\n".join(thirdlist))
        textfile.close()
    if thirdquestion == "slow-paced".casefold() or "slow".casefold() or "slowpaced".casefold() and thirdquestion != "bored".casefold():
        textfile = open("songlist.txt", "r")
        recommendcontent = textfile.readlines()
        for i in recommendcontent:
            thirdfindemotion = re.search(r"Emotion: (Bored)", i)
            if thirdfindemotion != None:
                thirdemotion = thirdfindemotion.group(1)
                if thirdemotion.casefold() == "Bored".casefold():
                    empowersongsearch = re.search(r"(^.*)", i)
                    if empowersongsearch != None:
                        songtrial = empowersongsearch.group(1)
                    thirdlist.append(songtrial)       
        print("\n".join(thirdlist))
        textfile.close()
        print("\n")
        print(f"Hope you enjoy this personalized recommendation list {username}")
        print("\n")

    cyclecontinue(selection, username)
    
    
    

    
    #unit test: makes sure that the tracks match what the user wants.
    pass

def altertracks(selection, username):
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
        tracknumber = re.search(r"([0-9]+).", i)
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
        altertracks(selection, username)
    else:
        print("Exiting track modification.")
    cyclecontinue(selection, username)


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
    randomset = random.sample(listData, 10)
    #just raises an error if there isn't enough songs here.
    if len(randomset) != 10:
        raise ValueError("There are not 10 songs in this list.")
    #print("\n".join(randomset))
    return(randomset)
    #offer users the chance to do over.
    #cyclecontinue(selection, username)

