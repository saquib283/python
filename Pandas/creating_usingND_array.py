import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel', 'Sophia', 'Michael', 'Olivia', 'Jacob', 'Grace'],
        'Age': [25, 30, 35, 23, 32, 24, 20, 29, 33, 31],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 40000, 30000, 670000, 670000, 56000, 680000, 340000, 560000, 570000]}
df = pd.DataFrame(data)
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
sum_salary = df['Salary'].sum()
max_age = df['Age'].max()
min_age = df['Age'].min()

print("Mean Salary : ", mean_salary)
print('Median Salary : ', median_salary)
print("sum of salary : ", sum_salary)
print("Maximum Age : ", max_age)
print("Minimum Age : ", min_age)
print("\n")
# Group By
print("Group bY :")

grouped_gender = df.groupby('Gender')
max_age_gender = grouped_gender['Age'].max()
total_salary_gender = grouped_gender['Salary'].sum()

print("Maximum Age By Gender : ", max_age_gender)
print("Total Salary By Gender : ", total_salary_gender)
print("\n")

# Sorting

print("sorting")
sorted_age = df.sort_values('Age')
print("Dataframe sorted By Age")
print(sorted_age)
print("\n")
sorted_salary = df.sort_values('Salary', ascending=False)
print("Dataframe sorted  By Salary")
print(sorted_salary)

print("\n")

# Deleting

print("Deleting")
newdf = df[df['Age'] > 25]
print(newdf)
df_column = df.drop('Salary', axis=1)
print(df_column)
