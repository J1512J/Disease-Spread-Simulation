#Student_Name : Venkata Karthikeya Ravilla
#Student_ID : 31116981
#Date_started : 06/06/2020
#Last_modified : 08/06/2020
"""
High Level Description: In this particular module we created a function visual_curve to plot the graph between Number of days and Patient count
"""

"""
scenario_A(Prediction): In case of scenario_A the results do match the predictions. This is a case where there are not many social distancing rules.
This is an uncontained outbreak. The cases increase exponentially.
This is because the meeting probability is 0.6 which is more than half.
Even though the number of days is small the meeting probability is high and even the health points are pretty low.
This is the reason why there is an uncontained outbreak in scenario_A.
"""

"""
scenario_B(Prediction): In case of scenario_B the results do match the predictions. This is a case where there are good social distancing rules.
This is an unpredictable situation. In this situation the sometimes the curve gets flattened in a day and sometimes it fluctuates.
The increase in cases is very less. This is due to low meeting probability compared to scenario_A.
Even though the number of days the simulation runs is more compared to scenario_A, having very high health points and low meeting probability results in this situation.
This is the reason why there is an unpredictable situation in scenario_B.
"""

"""
scenario_C(Prediction): In case of scenario_B the results do match the predictions. This is a case where there are excellent social distancing rules.
This is a flattening curve situation. In this situation the curve flattens soon after few days.
There is hardly any increase in cases. This is due to very very low meeting probability.
Even though the number of days the simulation runs is a lot, having very low meeting probability and good health points results in this situation.
This is the reason why there ia a flattening curve situation in scenarion_C.
"""



#here we are importing everthing from a2_31116981_task2 and also
#we are importing pyplot module as graph_plot from matplotlib library for plotting a graph
from a2_31116981_task2 import *
from matplotlib import pyplot as graph_plot


#the function visual_curve is created with the same parameters as run_simulation funtion but this function plots a graph
def visual_curve(days, meeting_probability, patient_zero_health):
    pt_count_list = run_simulation(days, meeting_probability, patient_zero_health)
    days_count_list = []
    for x in range(days):
        days_count_list.append(x)
    graph_plot.plot(days_count_list, pt_count_list)
    graph_plot.xlabel("Number Of Days")
    graph_plot.ylabel("Count of Patients")
    graph_plot.title("Meeting probability : " + str(meeting_probability * 100) + "%" + ", Number of Days : " + str(days) + ", Health Points : " + str(patient_zero_health))
#the graph_plot.show() displays the graph on the screen this is saved in png file format
    graph_plot.show()


#here all three parameters of visual_curve function are passed as the user inputs.
#Then the visual_curve function is called.
if __name__ == '__main__':
    days = int(input("Enter Number of Days : "))
    meeting_probability = float(input("Enter Meeting Probability : "))
    patient_zero_health = int(input("Enter Patient Zero Health : "))
    visual_curve(days, meeting_probability, patient_zero_health)
