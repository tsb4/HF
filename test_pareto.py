import numpy as np
import matplotlib.pyplot as plt

# Example data: each point is [number_of_parameters, accuracy]
data = np.array([
    [1000, 0.85],
    [1200, 0.90],
    [800, 0.80],
    [1500, 0.92],
    [1100, 0.87],
    [900, 0.88],
    [1300, 0.91],
    [950, 0.89]
])

def pareto_frontier(data):
    """
    Find the Pareto frontier from a given set of points.
    
    Args:
    - data: numpy array of points (each point is an array of objective values [number_of_parameters, accuracy])
    
    Returns:
    - numpy array of Pareto frontier points
    """
    num_points = data.shape[0]
    is_pareto = np.ones(num_points, dtype=bool)  # Initialize all points as Pareto optimal
    
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                # Check if point j dominates point i
                if (data[j][1] >= data[i][1] and data[j][0] <= data[i][0]) and \
                   (data[j][1] > data[i][1] or data[j][0] < data[i][0]):
                    is_pareto[i] = False
                    break

    return data[is_pareto]

pareto_points = pareto_frontier(data)

# Plotting the data points and Pareto frontier
plt.scatter(data[:, 0], data[:, 1], label="Data points")
plt.scatter(pareto_points[:, 0], pareto_points[:, 1], color='r', label="Pareto frontier")
plt.xlabel('Number of Parameters')
plt.ylabel('Accuracy')
plt.legend()
plt.title("Pareto Frontier (Maximizing Accuracy, Minimizing Number of Parameters)")
plt.show()

print("Pareto Frontier Points:\n", pareto_points)
