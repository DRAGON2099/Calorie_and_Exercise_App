#Packages needed 
import matplotlib.pyplot as plt

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
    5) Visualize Progress as a pie chart
    6) Visualize Progress as a bar chart
    7) Visualize Progress as a line graph
    8) Visualize Progress as numbers
    9) BMI Calculator
    10) Exercise Advisor

    0) Quit Menu
    ''')

    #choice variable dictates which menu option is implemented
    choice = int(input("Choose an option: "))

    #if first option i.e. the add breakfast consumption is chosen, this is implemented
    if choice == 1:
        print("Adding Breakfast consumption :- ")
        print()
        #lists to store the various food items and their various constituents
        food_items = []
        name_list = []
        calories_list = []
        fat_list = []
        protein_list = []
        carbs_list = []
        food_items_no = input("Enter no of items eaten : ")
        #to make sure the input is a number
        if  food_items_no.isnumeric():
            food_items_no = int(food_items_no)
        else:
            print("Error, please try again!")
            continue
        
        #for loop to input the food item and its various constituents in the above lists
        for i in range (food_items_no):
            name = input("Name of Food: ")
            name_list.append(name)
            print()
            calories = float(input("Enter amount of Calories: "))
            calories_list.append(calories)
            print()
            fat = float(input("Enter amount of Fat: "))
            fat_list.append(fat)
            print()
            protein = float(input("Enter amount of Protein: "))
            protein_list.append(protein)
            print()
            carbs = float(input("Enter amount of Carbs: "))
            carbs_list.append(carbs)
            print()

        food_items = [name_list,calories_list,fat_list,protein_list,carbs_list]
        #adding the various constituents together like fats in total in breakfast
        calories_breakfast = 0
        for a in range(len(calories_list)):
            calories_breakfast += calories_list[a]
        fat_breakfast = 0
        for b in range(len(fat_list)):
            fat_breakfast += fat_list[b]
        protein_breakfast = 0
        for c in range(len(protein_list)):
            protein_breakfast += protein_list[c]
        carbs_breakfast = 0
        for d in range(len(carbs_list)):
            carbs_breakfast += carbs_list[d]
        print('''In breakfast you have consumed the following :- ''')
        print()
        '''
        prints in the format 
        1) food item
        2) food item
        '''
        for j in range(len(name_list)):
            print(f"{j + 1})" + name_list[j])
            print()
        print()
        print("Calories consumed in Breakfast : " + str(calories_breakfast))
        print()
        print("Protein consumed in Breakfast : " + str(protein_breakfast))
        print()
        print("Fat consumed in Breakfast : " + str(fat_breakfast))
        print()
        print("Carbs consumed in Breakfast : " + str(carbs_breakfast))

    elif choice == 2:
        
        print("Adding Lunch consumption :- ")
        print()
        food_items = []
        name_list = []
        calories_list = []
        fat_list = []
        protein_list = []
        carbs_list = []
        food_items_no = input("Enter no of items eaten : ")
        if  food_items_no.isnumeric():
            food_items_no = int(food_items_no)
        else:
            print("Error, please try again!")
            continue

        for i in range (food_items_no):
            name = input("Name of Food: ")
            name_list.append(name)
            print()
            calories = float(input("Enter amount of Calories: "))
            calories_list.append(calories)
            print()
            fat = float(input("Enter amount of Fat: "))
            fat_list.append(fat)
            print()
            protein = float(input("Enter amount of Protein: "))
            protein_list.append(protein)
            print()
            carbs = float(input("Enter amount of Carbs: "))
            carbs_list.append(carbs)
            print()

        food_items = [name_list,calories_list,fat_list,protein_list,carbs_list]
        #adding the various constituents together like fats in total in breakfast
        calories_lunch = 0
        for a in range(len(calories_list)):
            calories_lunch += calories_list[a]
        fat_lunch = 0
        for b in range(len(fat_list)):
            fat_lunch += fat_list[b]
        protein_lunch = 0
        for c in range(len(protein_list)):
            protein_lunch += protein_list[c]
        carbs_lunch = 0
        for d in range(len(carbs_list)):
            carbs_lunch += carbs_list[d]
        print('''In Lunch you have consumed the following :- ''')
        print()
        for j in range(len(name_list)):
            print(f"{j + 1})" + name_list[j])
            print()
        print()
        print("Calories consumed in Lunch : " + str(calories_lunch))
        print()
        print("Protein consumed in Lunch : " + str(protein_lunch))
        print()
        print("Fat consumed in Lunch : " + str(fat_lunch))
        print()
        print("Carbs consumed in Lunch : " + str(carbs_lunch))

    #if first option i.e. the add breakfast consumption is chosen, this is implemented
    if choice == 3:
        print("Adding Snacks consumption :- ")
        print()
        #lists to store the various food items and their various constituents
        food_items = []
        name_list = []
        calories_list = []
        fat_list = []
        protein_list = []
        carbs_list = []
        food_items_no = input("Enter no of items eaten : ")
        #to make sure the input is a number
        if  food_items_no.isnumeric():
            food_items_no = int(food_items_no)
        else:
            print("Error, please try again!")
            continue
        
        #for loop to input the food item and its various constituents in the above lists
        for i in range (food_items_no):
            name = input("Name of Food: ")
            name_list.append(name)
            print()
            calories = float(input("Enter amount of Calories: "))
            calories_list.append(calories)
            print()
            fat = float(input("Enter amount of Fat: "))
            fat_list.append(fat)
            print()
            protein = float(input("Enter amount of Protein: "))
            protein_list.append(protein)
            print()
            carbs = float(input("Enter amount of Carbs: "))
            carbs_list.append(carbs)
            print()

        food_items = [name_list,calories_list,fat_list,protein_list,carbs_list]
        #adding the various constituents together like fats in total in breakfast
        calories_snacks = 0
        for a in range(len(calories_list)):
            calories_snacks += calories_list[a]
        fat_snacks = 0
        for b in range(len(fat_list)):
            fat_snacks += fat_list[b]
        protein_snacks = 0
        for c in range(len(protein_list)):
            protein_snacks += protein_list[c]
        carbs_snacks = 0
        for d in range(len(carbs_list)):
            carbs_snacks += carbs_list[d]
        print('''In Snacks you have consumed the following :- ''')
        print()
        '''
        prints in the format 
        1) food item
        2) food item
        '''
        for j in range(len(name_list)):
            print(f"{j + 1})" + name_list[j])
            print()
        print()
        print("Calories consumed in Snacks : " + str(calories_snacks))
        print()
        print("Protein consumed in Snacks : " + str(protein_snacks))
        print()
        print("Fat consumed in Snacks : " + str(fat_snacks))
        print()
        print("Carbs consumed in Snacks : " + str(carbs_snacks))

    elif choice == 0:
        print("Have a nice day!")
        done = True
