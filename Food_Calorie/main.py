#Packages needed 
from dataclasses import dataclass
import matplotlib.pyplot as plt

#Initializing name_goal variables for the various composition of food
calorie_goal = 0
protein_goal = 0
fat_goal = 0
carbs_goal = 0

#List to store the current day consumption food constituents i.e. everything eaten today containing what
current_day_consumption = []

#class Food to store the food and the various constituents and their amount
@dataclass
class Food:
    name: str
    calories: float
    protein: float
    fat: float
    carbs: float

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
    5) Visualize Progress as a pie chart
    6) Visualize Progress as a bar chart
    7) Visualize Progress as a line graph
    8) Visualize Progress as numbers
    9) BMI Calculator
    10) Exercise Advisor

    0) Quit Menu
    ''')

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Adding Breakfast consumption :- ")
        print()
        food_items = []
        food_items_no = input("Enter no of items eaten : ")
        if  food_items_no.isnumeric():
            food_items_no = int(food_items_no)
        else:
            print("Error, please try again!")
            continue

        for i in range (food_items_no):
            name = input("Name of Food: ")
            print()
            calories = float(input("Enter amount of Calories: "))
            print()
            fat = float(input("Enter amount of Fat: "))
            print()
            protein = float(input("Enter amount of Protein: "))
            print()
            carbs = float(input("Enter amount of Carbs: "))
            print()
            food = Food(name, calories, protein, fat, carbs)
            food_items.append(food)
            print("Successfully added!")
            print()

        print('''In breakfast you have consumed the following :- ''')
        print()
        print(food)
        print()
        '''name = input("Name of Food: ")
        calories = float(input("Enter amount of Calories: "))
        fat = float(input("Enter amount of Fat: "))
        protein = float(input("Enter amount of Protein: "))
        carbs = float(input("Enter amount of Carbs: "))
        food = Food(name, calories, protein, fat, carbs)
        current_day_consumption.append(food)
        print("Successfully added!")'''
    
    elif choice == 2:
        calorie_sum = sum(food.calories for food in current_day_consumption)
        protein_sum = sum(food.protein for food in current_day_consumption)
        fat_sum = sum(food.fat for food in current_day_consumption)
        carbs_sum = sum(food.carbs for food in current_day_consumption)

        labels = ["Protein", "Carbs", "Fat", "Calories"]
        values = [protein_sum, carbs_sum, fat_sum, calorie_sum]

        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Macronutrient Distribution")
        plt.show()

    elif choice == 0:
        print("Have a nice day!")
        done = True