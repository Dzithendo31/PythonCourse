import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Gender': ['Female', 'Male', 'Male', 'Male']}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Filtering data
male_df = df[df['Gender'] == 'Male']
print("\nMale DataFrame:")
print(male_df)

# Adding a new column
df['Profession'] = ['Engineer', 'Doctor', 'Artist', 'Teacher']
print("\nDataFrame with Profession:")
print(df)

# Sorting by Age
sorted_df = df.sort_values(by='Age')
print("\nSorted DataFrame by Age:")
print(sorted_df)
