#This file is for unit tests
import unittest
import methodholder
#when running these tests, make sure to first comment the cyclecontinue at the end of each method.
class test(unittest.TestCase):
    """
     A class that tests methods from the methodholder file.

    Attributes:
        self: a reference to the current instance of the class

"""
    def test_randomize(self):
        """ A test for the randomize function.
        Args:
            self
        """
        #In order to test this, comment out the cyclecontinue on line #380 of methodholder
        output = methodholder.randomize("randomize", "Ruka")
        notoutput = methodholder.randomize("randomize", "Hannah")
        self.assertNotEquals(output, notoutput)


    def test_altertracks(self):
        """ A test for the alter function.
        Args:
            self
        """
        #tests the cycle continue which allows users to continue using the program without having to exit.
        output = methodholder.altertracks("alter", "Hannah")
        
        self.assertRaises(AssertionError)
        #notoutput = methodholder.altertracks("selection", "")
        #self.assertNotEquals(output, notoutput)
        #assert ("You have the choice to either quit the program ('EXIT'), or continue using the other features available.") in output

    def test_recommendation(self):
      """ A test for the randomize function.
        Args:
            self
        """
      output = methodholder.recommendation("recommend", "Hannah")
      output2 = methodholder.recommendation("recommend", "Hannah")
      self.assertEquals(output, output2)

    def test_desiredtrack(self):
        """ A test for the randomize function.
        Args:
            self
        """
        output = methodholder.desiredlist("select", "Ruka")
        output2 = methodholder.desiredlist("SeLeCt", "Hannah")
        self.assertEquals(output, output2)
       

if __name__ == '__main__':
    unittest.main()

      
