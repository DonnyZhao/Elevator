# Elevator
A Python code base to simulate elevator. eg,  the elevator at floor 1, 1 person inside select to stop on 3, steps should be [UP_1, UP_1, OPEN_DOOR, CLOSE_DOOR]  

an elevator that can accept calls from  and plans the steps accordingly  moving outside without e.g. elevator at floor 1, 1 person outside call from floor 3 to go down to floor 1, steps should be [UP_1, UP_1, OPEN_DOOR, CLOSE_DOOR, Enter, Down_1,Down_1 ] 

Usage:
python elevator.py

Input parameters: 
number of floors(up to 30), number of customers(up to 30), number of elevators(1-2).

<img src="images/elevator_usage.png>

Expected result:

<img src="images/elevator_result_1.png>
<img src="images/elevator_result_2.png>
<img src="images/elevator_result_3.png>         

Exception:

1. The user input value should be a positive integer. 
2. THe user input value should be less pre-defined max value. 

<img src="images/elevator_usage.png>
          
Unit test:

<img src="images/elevator_Unit_test_result.png>
