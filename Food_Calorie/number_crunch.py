def numbers_data(cal, cal_goal, protein, protein_goal, fats, fats_goal, carbs, carbs_goal):
    cal_diff = cal_goal - cal
    if cal_diff > 0:
      print(f"You burnt {cal} Calories today and your goal was {cal_goal} Calories leaving a difference of {cal_diff}")
    elif cal_diff < 0:
      cal_diff = abs(cal_diff)
      print(f"You burnt {cal} Calories today and your goal was {cal_goal} Calories leaving an extra of {cal_diff} Calories Burnt") 
    protein_diff = protein_goal - protein
    if protein_diff > 0:
      print(f"You consumed {protein} grams of Protein today and your goal was {protein_goal} grams of Protein leaving a difference of {protein_diff}")   
    elif protein_diff < 0:
      protein_diff = abs(protein_diff)
      print(f"You consumed {protein} grams of Protein today and your goal was {protein_goal} grams of Protein leaving an excess of {protein_diff} grams of Protein Consumed")    
    fats_diff = fats_goal - fats 
    if fats_diff > 0:
      print(f"You consumed {fats} grams of Fat and your goal was {fats_goal} grams of fat leaving a difference of {fats_diff}")
    elif fats_diff < 0:
      fats_diff = abs(fats_diff)
      print(f"You consumed {fats} grams of Fat and your goal was {fats_goal} grams of fat leaving an excess of {fats_diff} grams of Fat consumed")
    carbs_diff = carbs_goal - carbs
    if carbs_diff > 0:
      print(f"You consumed {carbs} grams of Carbs today and your goal was {carbs_goal} grams of carbs leaving a difference of {carbs_diff}")      
    elif carbs_diff < 0:
      carbs_diff = abs(carbs_diff)
      print(f"You consumed {carbs} grams of Carbs today and your goal was {carbs_goal} grams of carbs leaving an excess of {carbs_diff} grams of Carbs consumed")      