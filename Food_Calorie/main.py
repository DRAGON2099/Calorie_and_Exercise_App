#Packages needed 
import matplotlib.pyplot as plt

#importing the other python files
from breakfast import breakfast
from lunch import lunch
from snacks import snacks
from dinner import dinner
from addl_food import addl_food
from bmi_calc import bmi_result

#For calculations and data purposes the total of everything
total_consumption = []

#Initializing name_goal variables for the various composition of food
calorie_goal = 0
protein_goal = 0
fat_goal = 0
carbs_goal = 0

done = False

while not done:
    #Menu that will print all the needed options
    print('''
    MENU :-

    1) Add Breakfast consumption 
    2) Add Lunch consumption
    3) Add Snacks consumption
    4) Add Dinner consumption
    5) Add additional Food consumption
    6) Visualize Progress as a pie chart
    7) Visualize Progress as a bar chart
    8) Visualize Progress as a line graph
    9) Visualize Progress as numbers
    10) BMI Calculator
    11) Exercise Advisor

    0) Quit Menu
    ''')

    #choice variable dictates which menu option is implemented
    choice = int(input("Choose an option: "))

    #if first option i.e. the add breakfast consumption is chosen, this is implemented
    if choice == 1:
        
         today_breakfast = breakfast()

    #if second option i.e. the add lunch consumption is chosen, this is implemented
    elif choice == 2:
        
        today_lunch = lunch()

    #if third option i.e. the add snacks consumption is chosen, this is implemented
    elif choice == 3:
        
        today_snacks = snacks()

    #if fourth option i.e. the add dinner consumption is chosen, this is implemented
    elif choice == 4:
        
        today_dinner = dinner()

    #if fifth option i.e. the add additional food consumption is chosen, this is implemented
    elif choice == 5:
        
        today_addl_food = addl_food()

    #if sixth option i.e. Visualize progress as pie chart is chosen, this is implemented
    elif choice == 6:
        
        pass    
    
    #if seventh option i.e. Visualize Progress as a bar chart is chosen, this is implemented
    elif choice == 7:
        
        pass   
    
    #if eighth option i.e. Visualize Progress as a line graph is chosen, this is implemented
    elif choice == 8:
        
        pass   
    
    #if ninth option i.e. Visualize Progress as numbers is chosen, this is implemented
    elif choice == 9:
        
        pass   
    
    #if tenth option i.e. BMI Calculator is chosen, this is implemented
    elif choice == 10:
        
        bmi_result()
    
    #if eleventh option i.e. Exercise Advisor is chosen, this is implemented
    elif choice == 11:
        
        pass 
    
    #if option 0 or quit is chosen this is implemented
    elif choice == 0:
        print("Have a nice day!")
        done = True
    
    #if any unvalid input is received for choice
    else:
        print("Sorry,Not a valid choice!")
        continue
