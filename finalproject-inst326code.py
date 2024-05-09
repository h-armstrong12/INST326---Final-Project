# Inst 326 (Ruka Ayele, Hannah Armstrong)
# Final Project - Emotion/Genre-Based Music Library Management and Recommendation System
# Goal: Develop a library management system that categorizes songs by both genre and the emotions
# they evoke, such as happiness, motivation, and relaxation.

import time
import methodholder  # Importing methodholder where key functions are stored.
import re
import unittest

# Prompt the user for their name which will be used throughout the session.
username = input("Enter the name you would like to be addressed as: ")
# Ensure the username is not empty. If it is, raise a ValueError.
if username == "":
    raise ValueError("There is no name")
    print("Please enter a name, we weren't able to catch what you typed in")

# Call the intro_username function to greet the user and explain the system's features.
methodholder.intro_username(username)

# Main loop: Let the user interact with the system repeatedly.
while True:
    # Ask the user what they would like to do within the system.
    selection = input("What would you like to do: ").lower()
    # Call the decision function which processes the user's choice.
    methodholder.decision(selection, username)
    # This checks if the user has chosen to interact with any of the main features.
    # Once a valid choice is made, we break from the loop.
    if selection in ["select", "recommend", "randomize", "alter"]:
        break

# The while loop above will continue to prompt the user until a valid command is entered.
# This structure ensures that the user is guided to make a correct choice and continues the interaction.
