# How to get number of rows in pandas dataframe
import pandas as pd
data = {
    "name": ["John", "Jane", "Jade"],
    "age": [2, 10, 3]
}
# print(data)
df = pd.DataFrame(data)
# print(df)

# Using len() function
num_of_rows = len(df)
print("1. Using len() function: ", end="")
print("The number of rows are {}".format(num_of_rows))

# Using shape attribute
# print(df.shape)
num_of_rows = df.shape[0]
print("1. Using df.shape attribute: ", end="")
print("The number of rows are {}".format(num_of_rows))