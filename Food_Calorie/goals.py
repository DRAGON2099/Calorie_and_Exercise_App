def goal():

  calories_goal = input("Please enter the amount of calories you want to burn : ")
  print()
    
  try:
    calories_goal = float(calories_goal)
  except ValueError:
    print("INVALID INPUT!")

  protein_goal = input("Please enter the amount of Protein you want to consume : ")
  print()

  try:
    protein_goal = float(protein_goal)
  except ValueError:
    print("INVALID INPUT!")

  fats_goal = input("Please enter the amount of Fat you want to consume : ")
  print()

  try:
    fats_goal = float(fats_goal)
  except ValueError:
    print("INVALID INPUT!")

  carbs_goal = input("Please enter the amount of Protein you want to consume : ")
  print()

  try:
    carbs_goal = float(carbs_goal)
  except ValueError:
    print("INVALID INPUT!")

  return calories_goal,protein_goal,fats_goal,carbs_goal
