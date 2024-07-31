import plotly.graph_objects as go

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
info = ["Point A", "Point B", "Point C", "Point D", "Point E"]

# Create a scatter plot
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers+lines', 
                                marker=dict(size=10),
                                text=info,  # Information for hover
                                hoverinfo='text+x+y'))

# Update layout for better visualization
fig.update_layout(title='Interactive Plot with Hover Information',
                  xaxis_title='X Axis',
                  yaxis_title='Y Axis')

# Save the interactive plot as an HTML file
file_path = 'tinteractive_plot.html'
fig.write_html(file_path)

# Display the plot in an interactive window (if needed)
# fig.show()

file_path

