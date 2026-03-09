# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 11))
# temperature = [random.randint(20, 40) for _ in days]

# plt.plot(days, temperature, marker='o', color='red', linestyle='-')

# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Random Temperature Data Graph")

# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

sales = np.random.randint(1000, 5000, 12)

plt.bar(months, sales, color="skyblue")

plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.title("Monthly Sales Data")

plt.show() 