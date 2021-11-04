#Student_Name : Venkata Karthikeya Ravilla
#Student_ID : 31116981
#Date_started : 04/06/2020
#Last_modified : 08/06/2020
"""High Level Description: In this particular module we create a patient class which has various methods
use the object created by the patient class i.e., patient_object then load patients into a list and the add friends to the list and then finally return the list.
then another function run_simulation is created to run the simulation according to the given parameters and then return the final result containing
the number of contagious cases by the end of each day and for each day in the form of a list.
"""


#here we are importing everthing from a2_31116981_task1 and also
#we are importing random module for random number generation in the program
from a2_31116981_task1 import *
import random

#Patient class is being created by inheriting Person class from a2_31116981_task1
class Patient(Person):
#since an additional parameter of health is added to the class we rewrite default __init__ method again
    def __init__(self, first_name, last_name, health):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
#by using the the following every version of Person class is being inherited
        Person.__init__(self,first_name,last_name)
#the method get_healthreturns the health of a patient in patient class
    def get_health(self):
        return self.health
#the method set_health sets the health of patient to new_health which is the parameter given in he method
    def set_health(self, new_health):
        self.health = new_health
#the method is_contagious returns a boolean value i.e., true if the person health is below 50 and returns false if equal to or greater than 50
    def is_contagious(self):
        if self.get_health() < 50:
            return True
        else:
            return False
#the method infect sets the health of a person with the current health by considering the formula given, this method takes one parameter viral_load
    def infect(self, viral_load):
        cur_health = 0
        if self.get_health() > 0:
            if self.health <= 29:
                cur_health = self.get_health() - (0.1 * viral_load)
            if self.health in range(30, 50):
                cur_health = self.get_health() - (1 * viral_load)
            if self.health > 49:
                cur_health = self.get_health() - (2 * viral_load)
        self.set_health(cur_health)
#the method sleep adds 5 health points to a persons health and make sures health never drops below 0 and goes above 100
    def sleep(self):
        self.health = self.health + 5
        if self.health >= 100:
            self.health = 100
        if self.health <= 0:
            self.health = 0


#the following is creation of load_patient() function which loads the people from the file a2_sample_set.txt
#the load_patient function is the exact same copy of load_people() function except that it takes one additional parameter initial health
#the following function opens a file named a2_sample_set.txt by only giving read permission
#an empty list pt_list is created for using in upcoming program
def load_patients(initial_health):
    open_file = open("a2_sample_set.txt", "r")
    the_file = open_file.read().splitlines()
    pt_list = []
# in the below code we split the data from the a2_samplw_set.txt file and create a Patient object with the name parameters being passed from the file and initial health as 75
# after creation of objects the file is being closed
    for people in the_file:
        names = people.split(": ")[0]
        first_name = names.split()[0]
        last_name = names.split()[1]
        patient_object = Patient(first_name, last_name,initial_health)
        pt_list.append(patient_object)
        open_file.close()
#here we reopen the same file and now again split the data in many different ways as per the requirement.
    open_file = open("a2_sample_set.txt", "r")
    the_file = open_file.read().splitlines()
#then we add the data of the point1 list to point list to point list by using extend() method which is a pre installed in python
    someone = 0
    for point in the_file:
        point1 = point.split(": ")[0]
        point2 = point.split(": ")[1].split(", ")
        point = [point1]
        point.extend(point2)
#now we are taking the index in range of len(point) which is the number of persons and friends in each line in the file a2_sample_set.txt
        for index in range(len(point)):
            if index > 0:
                thing = 0
#for each line in all 200 lines in the file, the index of point list is verifying the name at index of pt_list i.e., each friend in each line
#here pt_list[someone] is the the patient object for each patient. Friends are added to each patient object by using the add_friend method
                while thing in range(200):
                    if point[index] == pt_list[thing].get_name():
                        pt_list[someone].add_friend(pt_list[thing])
                    thing = thing + 1
        someone = someone + 1
#now we are closing the file below and returning the patient objects in the form of a list
    open_file.close()
    return pt_list


#below we created a run_simulation() functionwhich takes three parameters
#the first parameter days is number of days the simulation is run
#the second parameter meeting_probability which is the probability of meeting
#the third parameter is the patient_zero_health who is gonna spread the disease
#we are creating an empty list i.e., list_c to store the list of cases
#pt_list loads patients by calling load_patients() function by passing initial_health of 75
#in the following line gill bates i.e., patient_zero's, patient_zero_health is passed as a parameter in set_health method
def run_simulation(days, meeting_probability, patient_zero_health):
    list_c = []
    pt_list = load_patients(75)
    pt_list[0].set_health(patient_zero_health)
#for index in each day, the following is to be done
    for index in range(days):
        no_of_cases = 0
#for line in each line of 200 lines in the text file
        for line in range(200):
            pt_friends = pt_list[line].get_friends()
#for is_contagious() == false viral_load is 0
            viral_load = 0
#here we are adjusting the viral_load for contagious people i.e., patients
            pt_at_line = pt_list[line].is_contagious()
            if pt_at_line == True:
                viral_load = (310 + ((pt_list[line].get_health() - 25) ** 2))/62
#here we are setting up the meeting probability with random values
#the higher the meeting probability more the chance to spread the disease
            for f in range(len(pt_friends)):
                rand = random.random()
                if meeting_probability >= rand:
                    pt_friends[f].infect(viral_load)
#here we are iterating the number of cases depending on number of people contagious
        for index in range(200):
            pt_contagious = pt_list[index].is_contagious()
            if pt_contagious == True:
                no_of_cases = no_of_cases + 1
#we call this method for every patient or person to add health by 5 by calling sleep method from Patient class
        for index in range(200):
            pt_list[index].sleep()
#we are appending the total iterated cases into the list_c which is created at the very beginning of the function
#after appending the list_c is returned which contains the count of patients by the end of the day
        list_c.append(no_of_cases)
    return list_c

#here all three parameters of run_simulation function are passed as the user inputs.
#Then the run_simulation function is called and printed
if __name__ == '__main__':
    days = int(input("Enter Number of Days : "))
    meeting_probability = float(input("Enter Meeting Probability : "))
    patient_zero_health = int(input("Enter Patient Zero Health : "))
    test_sim = run_simulation(days, meeting_probability, patient_zero_health)
    print(test_sim)