import random
import unittest
import sys
from elevator import *

""" This application will test the simulate Elevator movement in Building with many floors and many Customers
    """

waiting_list = []           # Customers waiting to enter into the elevator

class Test_elevator(unittest.TestCase):

    # Test the floor class's input value
    # limit to 30 floors
    def test_floor_user_input(self):
        
        self.assertRaises(ValueError,user_input,-1)	
        self.assertRaises(ValueError,user_input,31)
        self.assertRaises(ValueError,user_input,29)
    
    # Test the Customer class's input value
    # limit to 30 persons per elevator
    def test_customer_user_input(self):
        self.assertRaises(ValueError,user_input,-1)
        self.assertRaises(ValueError,user_input,31)
        self.assertRaises(ValueError,user_input,29)

    # Test the Customer class's input value
    # limit to 30 persons per elevator

    def test_elevator_user_input(self):
       
        self.assertRaises(ValueError,user_input,-1)	
        self.assertRaises(ValueError,user_input,2)
        self.assertRaises(ValueError,user_input,3)