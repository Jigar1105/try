import pandas as pd
data={
    'id':[1,2,3,4,5,6,7,8,9,10],
    'Name':["John","Anna","Peter","Linda","James","Emily","Michael","Sarah","David","Laura"],
    'Age':[None,24,35,32,30,27,40,22,31,29],
    'dob':["1995-01-15","1999-05-30","1988-07-22","1991-11-10","1993-03-05","1996-09-18","1983-12-01","2001-04-25","1990-08-14","1992-02-20"],
    'gender':["M","F","M","F","M","F","M","F","M","F"],
    'phone':["1234567890","0987654321","5555555555","4444444444","3333333333","2222222222","1111111111","6666666666","7777777777","8888888888"],
    'science_score':[85,90,78,92,88,91,233,95,89,94],
    'math_score':[80,95,88,91,85,92,83,90,87,93],
    'ss_score':[82,88,85,89,84,90,81,92,86,91],
    'computer_score':[90,92,85,94,87,93,98,95,88,96],
    'total_score':[337,365,336,366,350,367,329,372,350,372],
    'percentage':[84.25,91.25,84.00,91.50,87.50,91.75,82.25,93.00,87.50,93.00],
    'grade':["A","A+","A","A+","B+","A+","B","A+","B+","A+"],
    'result':["Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass","Pass"]
}
df=pd.DataFrame(data)
print(df)
print("Age Mean:", df["Age"].mean())
print(df.mean(numeric_only=True))
scores = df[["science_score", "math_score", "ss_score", "computer_score"]]
print("Mean:\n", scores.mean())
print("\nMedian:\n", scores.median())
print("\nMode:\n", scores.mode())

print(df.isnull().sum())
print(df.duplicated())
print("Duplicate rows:", df.duplicated().sum())
print(df.describe())
print(df.head())
print(df.tail())
print(df.shape)
df.dropna(inplace=True)
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Age"] = df["Age"].fillna(25)
print(df)

# Fix science score
df["science_score"] = df["science_score"].clip(upper=100)

# Recalculate total
df["total_score"] = df[
    ["science_score", "math_score", "ss_score", "computer_score"]
].sum(axis=1)

# Recalculate percentage
df["percentage"] = df["total_score"] / 4

print(df["science_score"])