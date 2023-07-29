import pandas as pd

weather_data = {
    'day': ['1/2/2017', '2/2/2017', '3/2/2017', '4/02/2017', '5/2/2017', '6/2/2017', '7/2/2017'],
    'temperature': [23, 22, 21, 24, 23, 21, 22],
    'wind speed': [1, 4, 3, 2, 6, 4, 7],
    'event': ['Rain', 'sunny', 'snow', 'snow', 'Rain', 'Sunny', 'Sunny']
}
dataframe = pd.DataFrame(weather_data)
print(dataframe)
print("\n")
row, columns = dataframe.shape
print("The Shape of DataFrame is ", dataframe.shape)
print("The Number of Rows of the Dataframe is", row)
print("The Number of Rows of the Dataframe is", columns)
print("Initial few Rows of Dataframe is :")
print(dataframe.head(3))
print("\n")
print("Last few Rows of Dataframe is :")
print(dataframe.tail(3))
print("\n")

