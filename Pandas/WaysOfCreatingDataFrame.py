import pandas as pd

myData = {
    'name': ['rehan', 'cris', 'subham', 'soni', 'asiya', 'rohan'],
    'physics': [90, 78, 67, 87, 90, 78],
    'maths': [94, 87, 98, 69, 89, 90],
    'chemistry': [99, 89, 97, 87, 80, 78]

}
dataframe = pd.DataFrame(myData)
print(dataframe)

print(dataframe.max())
print(dataframe.max())
print(dataframe.columns) 
