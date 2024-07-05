from plotting import calculate_average
import matplotlib.pyplot as plt
import numpy as np

data = [90,90,80,60,51,61,81,92, 92] 

# Create histogram
plt.hist(data, bins=10, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Class Marks')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()

