import random
import sys

""" This application will simulate Elevator movement in Building with many floors and many Customers
    User should input custom number of floors and number of customers. Also, number of elevators (1 or 2)
    Application randomly creates start floor and and floor for each Customer
    Set up max number. floor =30, customer =30 and elevator=2"""

waiting_list = []           # Customers waiting to enter into the elevator

class Building:
    list_of_customers = []  # Array of Customers
    num_floors = 0          # Number of floors
    elevatorCount = 1       # Number of elevators
    
    elevator = 0
    elevator2 = 0

    def __init__(self, floors, customers, elevatorCnt):
        """ Initialise number of floors and number of customers """
        self.num_floors = floors
        self.elevatorCount = elevatorCnt
        global waiting_list

        for ID in range (1, customers+1):
            new_customer_instance = Customer(ID, self.num_floors)
            self.list_of_customers.append(new_customer_instance)

        waiting_list = self.list_of_customers
            
        self.elevator = Elevator(1, floors)
        if(self.elevatorCount == 2):
            self.elevator2 = Elevator(2, floors)
            self.elevator2.stop_floor = self.num_floors
        self.run()
    
    def run(self):
        """ Goal of simulation is that all customers reach end floor (destination floor)
        Main part of application is released in while loop stated below"""
        print ('\nELEVATOR SIMULATION STARTED!!!\n')
        number_of_customers = len(self.list_of_customers)
        if(self.elevatorCount == 2):
            while (self.elevator.customer_reached + self.elevator2.customer_reached) != number_of_customers:
                self.elevator.move()
                self.elevator2.move()
        else:
            while self.elevator.customer_reached != number_of_customers:
                self.elevator.move()
        
        print ('\nELEVATOR SIMULATION FINISHED!!!')
            

class Elevator:
    doorOpened = True        # Is Elevator Door opened or not
    elevatorNo = 0           # Elevator number
    total_floor_number = 0   # Number of Floors 
    direction = 1            # Direction will be 1 for UP and -1 for DOWN
    stop_floor = 1           # Floor on which is elevator currently. Starting from bottom 
    customer_reached = 0     # Number of customers reached to their destination
    max_floor = 0            # max destination floor of all customers

    def __init__(self, elNo, total_floor_number):
        self.total_floor_number = total_floor_number
        self.elevatorNo = elNo
        self.register_list = []       # Registered Customers who are inside elevator

    def move(self):
        """ This function moves Elevator. If elevator is on bottom or on top, elevator change direction
            When going UP, number of floors are increased by 1, if going down decreased by 1
            Checking on each floor for eventualy customer go out of elevator or get into elevator"""
        global waiting_list
            
        if(self.stop_floor == self.total_floor_number):
            self.direction = -1
        if(self.stop_floor == 1):
            self.direction = 1

        
        if(self.elevatorNo == 1):
            print ('\nElevator No: ', self.elevatorNo)
            print ('Floor: ', self.stop_floor)
        else:
            print ('\n\t\tElevator No: ', self.elevatorNo)
            print ('\t\tFloor: ', self.stop_floor)
        
        for customer in self.register_list:
            if(customer.end_floor == self.stop_floor):
                self.cancel_customer(customer)
        for customer in waiting_list:
            if(customer.start_floor == self.stop_floor):
                self.register_customer(customer)

        #check if direction is good
        self.get_max_dest_floor()
        if(self.max_floor < self.stop_floor):
            self.direction = -1
        else:
            self.direction = 1

        if(self.direction == 1):
            self.stop_floor = self.stop_floor + 1
        else:            
            self.stop_floor = self.stop_floor - 1 
        self.output()                

    def output(self):
        """ Prints stop flor, direction, list of customer in the elevator """
        if(self.elevatorNo == 1):
            if (self.doorOpened == True):
                print('CLOSE_DOOR')
                self.doorOpened = False
            if(self.direction == 1):
                print ('Moving direction: UP_1')
            else:
                print ('Moving direction: DOWN_1')
           
            print ('\n_________________________________________________________________________________')
        else:
            if (self.doorOpened == True):
                print('\t\tCLOSE_DOOR')
                self.doorOpened = False
            if(self.direction == 1):
                print ('\t\tMoving direction: UP_1')
            else:
                print ('\t\tMoving direction: DOWN_1')
            
            print ('\n\t\t_________________________________________________________________________________')

    def register_customer(self, customer):
        """ When Customer enter elevator he is in register_list and removed from waiting_list """
        global waiting_list
        self.register_list.append(customer)
        waiting_list.remove(customer)
        if(self.elevatorNo == 1):
            if (self.doorOpened == False):
                print('OPEN_DOOR')
                self.doorOpened = True
            print ('Customer with ID = ', customer.ID, ' enters into the elevator')
        else:
            if (self.doorOpened == False):
                print('\t\tOPEN_DOOR')
                self.doorOpened = True
            print ('\t\tCustomer with ID = ', customer.ID, ' enters into the elevator')
    
    def cancel_customer(self, customer):

        """ Customer leave elevator """
        global waiting_list
        customer.finished = True
        self.register_list.remove(customer)
        self.customer_reached = self.customer_reached + 1
        if(self.elevatorNo == 1):
            if (self.doorOpened == False):
                print('OPEN_DOOR')
                self.doorOpened = True
            print ('Customer with ID = ', customer.ID, ' left the elevator')
        else:
            if (self.doorOpened == False):
                print('\t\tOPEN_DOOR')
                self.doorOpened = True
            print ('\t\tCustomer with ID = ', customer.ID, ' left the elevator')
    
    def get_max_dest_floor(self):
        self.max_floor = 0
        global waiting_list
        #check registered customers
        for customer in self.register_list:
            if(customer.end_floor > self.max_floor):
                self.max_floor = customer.end_floor
        #check waiting list
        for customer in waiting_list:
            if(customer.start_floor > self.max_floor):
                self.max_floor = customer.start_floor

def user_input(message):
    """ Ensure that user are entered positive integer number """
    value = 0
    while(True):
        value = input(message)
		
        if(value.isdigit()):
            if( int(value) > 30 ):
                raise ValueError(' The max number should less than 30')
            else:
                break
        else:
            #print ('Please enter a postitive integer')
            raise ValueError('unexpected input. Please enter a postitive integer')
    return int(value)

class Customer:
    ID = 0
    start_floor = 0  # Start (Current)Floor - where Customer are when simulation started
    end_floor = 0    # End (Destination) Floor - where Customer should be after simulation finished
    finished = False

    def __init__(self, ID, number_of_floor):
        """ This function assign ID for the customer and randomly generate current floor and destination floor """
        self.ID = ID
        self.start_floor = random.randint(1, number_of_floor)
        self.end_floor = random.randint(1, number_of_floor)
        """ Make sure that current and destination floor are not the same """
        while self.end_floor == self.start_floor:
            self.end_floor = random.randint(1, number_of_floor)
        print ('Customer ID = ', self.ID, '\tStart Floor: ', self.start_floor, '\t End Floor: ', self.end_floor)


def main():
    print(" This script will generate random number to represent Start_floor and End_Floor")
    floors = user_input('Please enter the Max number of floors(1-30): ')
    customers = user_input('Please enter the number of customers(1-30): ')
    elevatorCnt = user_input('Please enter the number of elevators (1-2): ')
    if( elevatorCnt > 2 ):
        raise ValueError(' The max number should less than 3')
    else:
        building = Building(floors, customers, elevatorCnt)
        
if __name__ == "__main__":
    main()    
