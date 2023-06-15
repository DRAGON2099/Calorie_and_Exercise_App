def lunch():
    
    final_constituents = []

    while True:
        print("Adding Lunch consumption :- ")
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
        '''
        prints in the format 
        1) food item
        2) food item
        '''
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

        final_constituents = [calories_lunch, protein_lunch, fat_lunch, carbs_lunch]

        break

    return final_constituents