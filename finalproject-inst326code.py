"""
Inst 326 (Ruka Ayele, Hannah Armstrong)
Final Project - Emotion/Genre-Based Music Library Management and Recommendation System

Goal: We plan on developing a library management system that categorizes songs not only by
traditional metrics (e.g., genre) but also by the emotions or experiences they evoke (e.g.,
happiness, motivation, relaxation) in people.

"""
import time
import methodholder

#username input

username = input("Enter the name you would like to be adressed as: ")
if username == "":
    print("Please enter a name, we weren't able to catch what you typed in")
#unit test: make sure that the username is not empty, the user should input a name

methodholder.intro_username(username)

selection = input("What would you like to do: ")
if selection.lower == "select":
    methodholder.desiredlist
if selection.lower == "recommend":
    methodholder.recommendation
if selection.lower == "randomize":
    methodholder.randomize
if selection.lower == "alter":
    methodholder.altertracks
else:
    print("We were unable to identify what you typed it. Why dont you try again?")




#will ask users if they want to just look for music, find their musical tastes through a small quiz,
#alter some of the descriptive terms for each song (if they see fit) or generate a random playlist.


