import matplotlib.pyplot as plt
import numpy as np

dates = ['2024-1-15', '2024-1-15', '2024-1-16', '2024-1-17', '2024-1-17', '2024-1-17']
amounts = [500, 100, 323, 999, 278, 666]

# Create a unique index for each occurrence of the same date
date_indices = np.arange(len(dates))

# Create the bar plot
plt.bar(date_indices, amounts)

# Set x-axis labels as dates
plt.xticks(date_indices, dates, rotation=45)

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Rental Amounts by Date')

# Display the plot
plt.show()