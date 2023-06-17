import matplotlib.pyplot as plt

def pies(cal, cal_goal, protein, protein_goal, fats, fats_goal, carbs, carbs_goal):

  # Data for the first pie chart
  labels1 = ['Calories-Burnt', 'Protein-Consumed', 'Fat-Consumed', 'Carbs-Consumed']
  sizes1 = [cal, protein, fats, carbs]

  # Data for the second pie chart
  labels2 = ['Calorie-Goal', 'Protein-Goal', 'Fat-Goal', 'Carb-Goal']
  sizes2 = [cal_goal, protein_goal, fats_goal, carbs_goal]

  # Create the figure and axes
  fig, (ax1, ax2) = plt.subplots(1, 2)

  # Plot the first pie chart
  ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%')
  ax1.set_title('Current Progress')

  # Plot the second pie chart
  ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%')
  ax2.set_title('Goals')

  # Adjust the spacing between subplots
  fig.tight_layout()

  # Display the chart
  plt.show()

