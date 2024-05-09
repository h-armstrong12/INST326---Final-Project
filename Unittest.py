#This file is for unit tests

import unittest
import methodholder

class test(unittest.TestCase):
    def test_randomize(self):
        # Call the function and get the returned strings
        output = methodholder.randomize("randomize", "Ruka")
        notoutput = methodholder.randomize("randomize", "Hannah")
        self.assertNotEquals(output, notoutput)
        # Check if the expected strings are returned
        
        #assert ("Hello there!") in output
        #assert ("Here is a randomized list of 10 songs from the songlist file.") in output
        #print("successful")


    #def test_cyclecontinue(self):
         #tests the cycle continue which allows users to continue using the program without having to exit.
         #output = methodholder.cyclecontinue("selection", "Ruka")
         #self.assertRaises()
         #assert ("You have the choice to either quit the program ('EXIT'), or continue using the other features available.") in output
         #print("successful")

    #def test_altertracks():
         #output = methodholder.altertracks("alter", "Hannah")
         #assert("Exiting track modification.") in output
         #print("successful")

    def test_recommendation(self):
        output = methodholder.recommendation("somethingelse", "Hannah")
        input = methodholder.recommendation("reommend", "Hannah")
        self.assertNotEquals(output, input)
      #if methodholder.recommendation(selection="recommend") is False:
       #  print("error")

    #     pass
        

if __name__ == '__main__':
    unittest.main()
    #test_randomize()
    #  test_cyclecontinue()
    #  test_altertracks()
    #test_recommendation()

      
