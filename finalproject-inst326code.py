"""
Inst 326 (Ruka Ayele, Hannah Armstrong)
Final Project - Emotion/Genre-Based Music Library Management and Recommendation System

Goal: We plan on developing a library management system that categorizes songs not only by
traditional metrics (e.g., genre) but also by the emotions or experiences they evoke (e.g.,
happiness, motivation, relaxation) in people.

"""
import time
import methodholder
import re
import unittest

#username input
username = input("Enter the name you would like to be adressed as: ")
if username == "":
    #raise value: make sure that the username is not empty, the user should input a name
    raise ValueError("There is no name")
    print("Please enter a name, we weren't able to catch what you typed in")

methodholder.intro_username(username)

while True:
    selection = input("What would you like to do: ").lower()
    methodholder.decision(selection, username)
    if str(selection) == "select" or "recommend" or "randomize" or "alter":
        break
    




#will ask users if they want to just look for music, find their musical tastes through a small quiz,
#alter some of the descriptive terms for each song (if they see fit) or generate a random playlist.


