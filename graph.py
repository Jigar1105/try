# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 31))
# temperature = [random.randint(20, 40) for _ in days]

# plt.plot(days, temperature, marker='o', color='red', linestyle='-')

# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Random Temperature Data Graph")

# plt.grid(True)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# months = ["Jan","Feb","Mar","Apr","May","Jun",
#           "Jul","Aug","Sep","Oct","Nov","Dec"]

# sales = np.random.randint(1000, 5000, 12)

# plt.bar(months, sales, color="skyblue")

# plt.xlabel("Month")
# plt.ylabel("Sales Amount")
# plt.title("Monthly Sales Data")

# plt.show() 


# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 31))

# temperatures = [random.randint(20, 40) for _ in range(30)]

# max_temp = max(temperatures)
# max_day = days[temperatures.index(max_temp)]

# plt.plot(days, temperatures, marker='o', label="Temperature")

# plt.scatter(max_day, max_temp, color='red', s=100, label="Highest Temperature")

# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("30 Day Temperature Graph")
# plt.legend()

# plt.grid(True)

# plt.show()

import random
import matplotlib.pyplot as plt

days = list(range(1, 31))

income = [random.randint(1000, 5000) for _ in days]
expense = [random.randint(500, 4000) for _ in days]

plt.plot(days, income, color='green', label="Income")   
plt.plot(days, expense, color='red', label="Expense")

plt.xlabel("Day")
plt.ylabel("Amount")
plt.title("30 Days Income vs Expense")
plt.legend()
plt.grid(True)

plt.show()


# import matplotlib.pyplot as plt

# months = ["Jan","Feb","Mar","Apr","May","Jun",
#           "Jul","Aug","Sep","Oct","Nov","Dec"]

# income = [3000,3200,3100,3500,3700,4000,4200,4100,3900,4500,4700,5000]
# expense = [2500,2600,2700,2900,3000,3200,3400,3300,3100,3600,3800,4000]

# plt.bar(months, expense, color='red', alpha=0.6, label="Expense")

# plt.plot(months, income, marker='o', color='green', label="Income")

# plt.xlabel("Month")
# plt.ylabel("Amount ($)")
# plt.title("Monthly Income vs Expense Tracker")

# plt.legend()
# plt.grid(True)

# plt.show()

# import random
# import matplotlib.pyplot as plt
 
# students = ["Aman", "Rahul", "Priya", "Neha", "Arjun"]

# math_marks = [random.randint(40, 100) for _ in students]
# science_marks = [random.randint(40, 100) for _ in students]
# english_marks = [random.randint(40, 100) for _ in students]

# plt.plot(students, math_marks, marker='o', label="Math")
# plt.plot(students, science_marks, marker='o', label="Science")
# plt.plot(students, english_marks, marker='o', label="English")

# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Student Marks Analysis (Line Chart)")

# plt.legend()
# plt.grid(True)

# plt.show()


# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 31))

# steps = [random.randint(4000, 12000) for _ in days]
# calories = [random.randint(1800, 3000) for _ in days]
# weight = [round(random.uniform(65, 75), 1) for _ in days]

# plt.plot(days, steps, marker='o', label="Steps per Day")
# plt.plot(days, calories, marker='o', label="Calories Burned")
# plt.plot(days, weight, marker='o', label="Weight (kg)")

# plt.xlabel("Day")
# plt.ylabel("Value")
# plt.title("30-Day Fitness Tracking")

# plt.legend()
# plt.grid(True)
# plt.show()