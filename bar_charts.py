import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")


flight_filepath = "../input/flight_delays.csv"

# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Print the data
flight_data


# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")



# sns.barplot - This tells the notebook that we want to create a bar chart.
# Remember that sns refers to the seaborn package, 
# and all of the commands that you use to create charts in this course will start with this prefix.
# x=flight_data.index - This determines what to use on the horizontal axis.
# In this case, we have selected the column that indexes the rows (in this case, the column containing the months).
# y=flight_data['NK'] - This sets the column in the data that will be used to determine the height of each bar. 
# In this case, we select the 'NK' column.




# heatmaps



# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")

# sns.heatmap - This tells the notebook that we want to create a heatmap.
# data=flight_data - This tells the notebook to use all of the entries in flight_data to create the heatmap.
# annot=True - This ensures that the values for each cell appear on the chart. 
# (Leaving this out removes the numbers from each of the cells!)








