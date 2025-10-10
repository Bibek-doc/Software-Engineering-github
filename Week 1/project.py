import numpy as np
temp_celsius = np.array( [18.5, 19, 20, 25.0, 2, 30, 13.9])

average_temp = np.mean(temp_celsius)

print(f"Average temeprature of the Month: {average_temp : .2f} C")

max_temp = np.max(temp_celsius)
min_temp = np.min(temp_celsius)

print(f"    : { average_temp}")