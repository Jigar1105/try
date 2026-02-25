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