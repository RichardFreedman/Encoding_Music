import os
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# Create "images" directory if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Bar Chart - Plotly
categories = ['Product A', 'Product B', 'Product C']
sales = [100, 150, 120]

fig = go.Figure(data=[go.Bar(x=categories, y=sales)])

fig.update_layout(
    title="Sales by Product Category",
    xaxis_title="Product",
    yaxis_title="Sales"
)

fig.write_image("images/bar_chart_plotly.svg")

# Bar Chart - Matplotlib
import matplotlib.pyplot as plt

plt.bar(categories, sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales by Product Category")
plt.savefig("images/bar_chart_matplotlib.svg")
plt.close()

# Histogram - Plotly
np.random.seed(0)
scores = np.random.normal(70, 10, 100)

fig = go.Figure(data=[go.Histogram(x=scores)])

fig.update_layout(
    title="Distribution of Exam Scores",
    xaxis_title="Score",
    yaxis_title="Count"
)

fig.write_image("images/histogram_plotly.svg")

# Histogram - Matplotlib
plt.hist(scores)
plt.xlabel("Score")
plt.ylabel("Count")
plt.title("Distribution of Exam Scores")
plt.savefig("images/histogram_matplotlib.svg")
plt.close()

# Scatter Plot - Plotly
study_hours = [3, 4, 2, 5, 6, 5, 3, 4, 2, 6]
exam_scores = [70, 80, 65, 90, 95, 85, 75, 80, 70, 90]

fig = go.Figure(data=go.Scatter(x=study_hours, y=exam_scores, mode='markers'))

# Perform linear regression
regression = LinearRegression()
regression.fit(np.array(study_hours).reshape(-1, 1), exam_scores)
regression_line = regression.predict(np.array(study_hours).reshape(-1, 1))

fig.add_trace(go.Scatter(x=study_hours, y=regression_line, mode='lines', name='Regression Line'))

fig.update_layout(
    title="Exam Scores vs Study Hours",
    xaxis_title="Study Hours",
    yaxis_title="Exam Scores",
    hovermode='closest'
)

fig.write_image("images/scatter_plot_plotly.svg")

# Scatter Plot - Matplotlib
plt.scatter(study_hours, exam_scores)
plt.plot(study_hours, regression_line, color='red', label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")

# Calculate correlation coefficient
correlation, _ = pearsonr(study_hours, exam_scores)
correlation_text = "Correlation: {:.2f}".format(correlation)

plt.annotate(correlation_text, (max(study_hours) - 1.75, max(exam_scores)-4), color='red')

plt.title("Exam Scores vs Study Hours")
plt.legend()
plt.savefig("images/scatter_plot_matplotlib.svg")
plt.close()

# Correlation Plot - Plotly
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

correlation_matrix = np.corrcoef(x, y)
correlation = correlation_matrix[0, 1]

fig = go.Figure(data=go.Heatmap(z=correlation_matrix, x=['Variable X', 'Variable Y'], y=['Variable X', 'Variable Y']))
fig.update_layout(
    title=f'Correlation: {correlation:.2f}',
    xaxis_title="Variable",
    yaxis_title="Variable",
)

fig.write_image("images/correlation_plot_plotly.svg")

# Correlation Plot - Matplotlib
plt.scatter(x, y)
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.title("Correlation Plot")
plt.savefig("images/correlation_plot_matplotlib.svg")
plt.close()
