import matplotlib.pyplot as plt

def bars(cal, cal_goal, protein, protein_goal, fats, fats_goal, carbs, carbs_goal):
    x_bar = ['Calories Burnt(cal)', 'Calorie-Goal(cal)', 'Protein-Consumed(g)', 'Protein-Goal(g)', 'Fats-Consumed(g)', 'Fats-Goal(g)', 'Carbs-Consumed(g)', 'Carbs-Goal(g)']
    y_bar = [cal, cal_goal, protein, protein_goal, fats, fats_goal, carbs, carbs_goal]

    # Create a list of colors for the bars
    colors = ['blue', 'blue', 'red', 'red', 'green', 'green', 'yellow', 'yellow']

    # Create the bar graph with different colors
    plt.bar(x_bar, y_bar, color=colors)

    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Graph Progress')

    # Display the graph
    plt.show()

