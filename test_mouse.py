import matplotlib.pyplot as plt
import mplcursors

# Sample data
models = [
    {'name': 'Model A', 'created_at': '2022-01-01', 'downloads': 1000, 'likes': 150, 'accuracy': 0.85, 'parameters': 1e6},
    {'name': 'Model B', 'created_at': '2022-02-01', 'downloads': 1500, 'likes': 250, 'accuracy': 0.90, 'parameters': 2e6},
    {'name': 'Model C', 'created_at': '2022-03-01', 'downloads': 2000, 'likes': 350, 'accuracy': 0.92, 'parameters': 3e6},
    {'name': 'Model D', 'created_at': '2022-04-01', 'downloads': 2500, 'likes': 450, 'accuracy': 0.93, 'parameters': 4e6},
]

# Extract data for plotting
accuracies = [model['accuracy'] for model in models]
parameters = [model['parameters'] for model in models]

# Create the plot
fig, ax = plt.subplots()
scatter = ax.scatter(parameters, accuracies)

# Add labels and title
ax.set_xlabel('Number of Parameters')
ax.set_ylabel('Accuracy')
ax.set_title('Model Performance')

# Function to format the annotation text
def format_annotation(index):
    model = models[index]
    return (
        f"Name: {model['name']}\n"
        f"Created at: {model['created_at']}\n"
        f"Downloads: {model['downloads']}\n"
        f"Likes: {model['likes']}"
    )

# Add interactive annotations
cursor = mplcursors.cursor(scatter, hover=True)
@cursor.connect("add")
def on_add(sel):
    sel.annotation.set_text(format_annotation(sel.index))

# Show plot
plt.show()
