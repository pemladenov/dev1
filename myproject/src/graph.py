#run the env: myenv\Scripts\activate

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Simple Line Plot')

# Show plot
plt.show()