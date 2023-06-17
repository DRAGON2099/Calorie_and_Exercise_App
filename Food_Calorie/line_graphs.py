import plotly.graph_objects as go
import matplotlib.pyplot as plt

def lines(cal, cal_goal, protein, protein_goal, fats, fats_goal, carbs, carbs_goal):

  #data
  x = [cal, protein, fats, carbs]
  y = [cal_goal, protein_goal, fats_goal, carbs_goal]

  # Create a figure
  fig = go.Figure()

  # Add a line trace
  fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Line'))

  # Set labels and title
  fig.update_layout(xaxis_title='Current Progress', yaxis_title='Goals', title='Line Graph')

  # Display the graph
  fig.show()

  # Create a figure and axis
  fig, ax = plt.subplots()

  # Plot the line
  ax.plot(x, y, linestyle='-', color='b')

  # Plot the data points with highlights
  ax.plot(x, y, marker='o', linestyle='', markersize=8, color='r', label='Data Points')

  # Set labels and title
  ax.set_xlabel('Current Progress')
  ax.set_ylabel('Goals')
  ax.set_title('Line Graph')

  # Display the legend
  ax.legend()

  # Display the graph
  plt.show()

