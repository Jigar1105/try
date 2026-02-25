import pandas as pd
from tabulate import tabulate

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)

# Full DataFrame
print(tabulate(df, headers='keys', tablefmt='psql'))

# Single row (correct way)
print("\nSingle Row:")
print(tabulate(df.loc[[1]], headers='keys', tablefmt='psql'))

# Multiple rows
print("\nMultiple Rows:")
print(tabulate(df.loc[[1,2]], headers='keys', tablefmt='psql')) 


# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 
# print(df.loc["day2"])

# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar)

import pandas as pd
df=pd.read_csv("employee_data.csv")
print(df)
