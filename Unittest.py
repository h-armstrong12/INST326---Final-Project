#This file is for unit tests

import unittest
import methodholder


def test_randomize():
    # Call the function and get the returned strings
    output = methodholder.randomize("randomize", "Ruka")

    # Check if the expected strings are returned
    
    assert ("Hello there!") in output
    assert ("Here is a randomized list of 10 songs from the songlist file.") in output
    print("successful")


def test_cyclecontinue():
    #tests the cycle continue which allows users to continue using the program without having to exit.
    output = methodholder.cyclecontinue("selection", "Ruka")
    
    assert ("You have the choice to either quit the program ('EXIT'), or continue using the other features available.") in output
    print("successful")

def test_altertracks():
    output = methodholder.altertracks("alter", "Hannah")
    assert("Exiting track modification.") in output
    print("successful")

def test_recommendation():
    output = methodholder.recommendation("somethingelse", "Hannah")
    if methodholder.recommendation(selection="recommend") is False:
        print("error")
        

if __name__ == '__main__':
 #   test_randomize()
  #  test_cyclecontinue()
  #  test_altertracks()
    test_recommendation()




      
