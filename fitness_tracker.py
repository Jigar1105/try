import pymysql
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# -----------------------------
# DATABASE CONNECTION
# -----------------------------

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="fitness_tracker"
)

cursor = db.cursor()

# -----------------------------
# CHECK IF DATA EXISTS
# -----------------------------

cursor.execute("SELECT COUNT(*) FROM fitness_data")
count = cursor.fetchone()[0]

# -----------------------------
# INSERT RANDOM DATA
# -----------------------------

if count == 0:

    for day in range(1,31):

        steps = random.randint(4000,12000)
        calories = random.randint(1800,3000)
        weight = round(random.uniform(65,75),1)

        sql = """
        INSERT INTO fitness_data (day,steps,calories,weight)
        VALUES (%s,%s,%s,%s)
        """

        val = (day,steps,calories,weight)

        cursor.execute(sql,val)

    db.commit()

    print("Data inserted into MySQL database")

# -----------------------------
# LOAD DATA FROM DATABASE
# -----------------------------

query = "SELECT * FROM fitness_data"
df = pd.read_sql(query, db)

print("\nFitness Data Preview\n")
print(df.head())

# -----------------------------
# ANALYTICS
# -----------------------------

print("\nAnalytics\n")

print("Average Steps:", round(df["steps"].mean()))
print("Average Calories:", round(df["calories"].mean()))
print("Average Weight:", round(df["weight"].mean(),1))

# -----------------------------
# GRAPH
# -----------------------------

plt.figure(figsize=(10,6))

plt.plot(df["day"], df["steps"], label="Steps")
plt.plot(df["day"], df["calories"], label="Calories")
plt.plot(df["day"], df["weight"], label="Weight")

plt.xlabel("Day")
plt.ylabel("Value")
plt.title("30 Day Fitness Dashboard")

plt.legend()
plt.grid(True)

plt.show()

# -----------------------------
# AI WEIGHT PREDICTION
# -----------------------------

X = df[["day"]]
y = df["weight"]

model = LinearRegression()
model.fit(X,y)

future_days = np.array([[31],[32],[33],[34],[35]])

predicted_weight = model.predict(future_days)

print("\nPredicted Weight for Next 5 Days\n")

for d,w in zip(range(31,36), predicted_weight):
    print(f"Day {d}: {round(w,2)} kg")

# -----------------------------

cursor.close()
db.close()