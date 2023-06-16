def exercise():
    
    weight_kg = input("Please enter your weight in kgs : ")
    print()
    
    try:
      weight_kg = float(weight_kg)
    except ValueError:
      print("INVALID INPUT!")   

    aerobics = 5.0
    cycling = 8.0
    running = 10.0
    swimming = 6.0
    walking = 3.5

    exercise = input('''The following are general exercises which are doable for all age groups having an effectiveness value on our custom scale for burning calories:-

    1) Aerobics - Has an effectiveness value of 5
    2) Cycling - Has an effectiveness value of 8
    3) Running - Has an effectiveness value of 10
    4) Swimming - Has an effectiveness value of 6
    5) Walking - Has an effectiveness value of 3.5

    Please enter name/no. of your choice of exercise from above : ''')
    print()

    exercise = exercise.lower()

    calories_per_minute = 0.0

    if exercise == "aerobics" or 1:
        calories_per_minute = 0.0875 * (weight_kg)
    elif exercise == "cycling" or 2:
        calories_per_minute = 0.14 * (weight_kg)
    elif exercise == "running" or 3:
        calories_per_minute = 0.175 * (weight_kg)
    elif exercise == "swimming" or 4:
        calories_per_minute = 0.105 * (weight_kg)
    elif exercise == "walking" or 5:
        calories_per_minute = 0.06125 * (weight_kg)
    
    duration = input("Please enter in minutes the duration for which you choose to exercise : ")
    print()

    try:
      duration = float(duration)
    except ValueError:
      print("INVALID INPUT!")    

    total_cal = 0

    total_cal = calories_per_minute * duration

    print(f"For the duration of {duration} minutes you will lose {total_cal} Calories!")
    print()

    return total_cal
