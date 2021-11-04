#Student_Name : Venkata Karthikeya Ravilla
#Student_ID : 31116981
#Date_started : 03/06/2020
#Last_modified : 08/06/2020
"""High Level Description: In this particular module we create a person class which has various methods
use the object created by the person class i.e., person_object then load people into a list and the add friends to the list and then finally return the list
"""


#creating a person class and passing first_name and last_name as parameters.
class Person:
#the init method is a default sytax to create a class. In this method we created instance variables by using self.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friend_person = []
#add_friend method appends or adds a friend to friend_person list. The parameter friend_person is being appended.
    def add_friend(self, friend_person):
        self.friend_person.append(friend_person)
#the below method get_name gets the name of a person and returns full name after concatenation of first_name and last_name
    def get_name(self):
        name = str(self.first_name) + " " + str(self.last_name)
        return name
#the following method get_friends returns the name list of friends appended to the friend_person list
    def get_friends(self):
        return self.friend_person


#the following is creation of load_people() function which loads the people from the file a2_sample_set.txt
#the following function opens a file named a2_sample_set.txt by only giving read permission
#an empty list pr_list is created for using in upcoming program
def load_people():
    open_file = open("a2_sample_set.txt", "r")
    the_file = open_file.read().splitlines()
    pr_list = []
#in the below code we split the data from the a2_samplw_set.txt file and create a Person object with the parameters being passed from the file
#after creation of objects the file is being closed
    for people in the_file:
        names = people.split(": ")[0]
        first_name = names.split()[0]
        last_name = names.split()[1]
        person_object = Person(first_name, last_name)
        pr_list.append(person_object)
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
#for each line in all 200 lines in the file, the index of point list is verifying the name at index of pr_list i.e., each friend in each line
#here pr_list[someone] is the the person object for each person. Friends are added to each person object by using add_friend method
                while thing in range(200):
                    if point[index] == pr_list[thing].get_name():
                        pr_list[someone].add_friend(pr_list[thing])
                    thing = thing + 1
        someone = someone + 1
#now we are closing the file below and returning the person objects in the form of a list
    open_file.close()
    return pr_list


#here the load_people() function in called and the program is executed in the if statement
if __name__ == '__main__':
    load_people()

