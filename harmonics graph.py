import matplotlib.pyplot as plt
import numpy as np

# Define the number of terms in the harmonic series
n_terms = 10000

# Create an array of n values for the harmonic series (from 1 to n_terms)
n = np.arange(1, n_terms + 1)

# Calculate the corresponding y values for the harmonic series (partial sums)
y = np.cumsum(1 / n)

# Create a plot
plt.plot(n, y, label='Partial Sums of Harmonic Series', color='r')

# Add labels and a legend
plt.xlabel('n')
plt.ylabel('Partial Sum of 1/n')
plt.title('Harmonic Series (Partial Sums)')
plt.legend()

# Show the plot
plt.show()
