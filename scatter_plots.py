# Path of the file to read
insurance_filepath = "../input/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

insurance_data.head()


sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])



# To double-check the strength of this relationship, you might like to add a regression line, 
# or the line that best fits the data. We do this by changing the command to sns.regplot.
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])



# We can use scatter plots to display the relationships between (not two, but...) three variables! 
# One way of doing this is by color-coding the points.

# For instance, to understand how smoking affects the relationship between BMI and insurance costs, 
# we can color-code the points by 'smoker', and plot the other two columns ('bmi', 'charges') on the axes.
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])



# we can use the sns.lmplot command to add two regression lines, 
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
# The sns.lmplot command above works slightly differently than the commands you have learned about so far:

# Instead of setting x=insurance_data['bmi'] to select the 'bmi' column in insurance_data, 
# we set x="bmi" to specify the name of the column only.
# Similarly, y="charges" and hue="smoker" also contain the names of columns.
# We specify the dataset with data=insurance_data.

	


# categorical scatter plot,

sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])



