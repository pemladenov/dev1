#run the env: myenv\Scripts\activate

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Erstellen vom plot
plt.plot(x, y)

#labels
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simpler Plot')

# Show plot
plt.show()
