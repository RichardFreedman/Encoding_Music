# Bar Chart - Plotly
import altair_saver
import plotly.graph_objects as go

categories = ['Product A', 'Product B', 'Product C']
sales = [100, 150, 120]

fig = go.Figure(data=[go.Bar(x=categories, y=sales)])

fig.write_image("bar_chart_plotly.svg")


# Bar Chart - Matplotlib
import matplotlib.pyplot as plt

categories = ['Product A', 'Product B', 'Product C']
sales = [100, 150, 120]

plt.bar(categories, sales)
plt.savefig("bar_chart_matplotlib.svg")



# Bar Chart - Altair
import altair as alt
import pandas as pd

data = pd.DataFrame({'categories': ['Product A', 'Product B', 'Product C'],
                     'sales': [100, 150, 120]})

alt.Chart(data).mark_bar().encode(x='categories', y='sales').interactive().save("bar_chart_altair.svg")


# Histogram - Plotly
import plotly.graph_objects as go
import numpy as np

np.random.seed(0)
scores = np.random.normal(70, 10, 100)

fig = go.Figure(data=[go.Histogram(x=scores)])

fig.write_image("histogram_plotly.svg")


# Histogram - Matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
scores = np.random.normal(70, 10, 100)

plt.hist(scores)
plt.savefig("histogram_matplotlib.svg")



# Histogram - Altair
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(0)
scores = np.random.normal(70, 10, 100)

data = pd.DataFrame({'scores': scores})

alt.Chart(data).mark_bar().encode(x=alt.X('scores', bin=alt.Bin(step=5)), y='count()').interactive().save("histogram_altair.svg")


# Scatter Plot - Plotly
import plotly.graph_objects as go

study_hours = [3, 4, 2, 5, 6, 5, 3, 4, 2, 6]
exam_scores = [70, 80, 65, 90, 95, 85, 75, 80, 70, 90]

fig = go.Figure(data=go.Scatter(x=study_hours, y=exam_scores, mode='markers'))

fig.write_image("scatter_plot_plotly.svg")


# Scatter Plot - Matplotlib
import matplotlib.pyplot as plt

study_hours = [3, 4, 2, 5, 6, 5, 3, 4, 2, 6]
exam_scores = [70, 80, 65, 90, 95, 85, 75, 80, 70, 90]

plt.scatter(study_hours, exam_scores)
plt.savefig("scatter_plot_matplotlib.svg")


# Scatter Plot - Altair
import altair as alt
import pandas as pd

study_hours = [3, 4, 2, 5, 6, 5, 3, 4, 2, 6]
exam_scores = [70, 80, 65, 90, 95, 85, 75, 80, 70, 90]

data = pd.DataFrame({'study_hours': study_hours, 'exam_scores': exam_scores})

alt.Chart(data).mark_circle().encode(x='study_hours', y='exam_scores').interactive().save("scatter_plot_altair.svg")


# Correlation Plot - Plotly
import plotly.graph_objects as go
import numpy as np

np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

correlation_matrix = np.corrcoef(x, y)
correlation = correlation_matrix[0, 1]

fig = go.Figure(data=go.Heatmap(z=correlation_matrix, x=['Variable X', 'Variable Y'], y=['Variable X', 'Variable Y']))
fig.update_layout(title=f'Correlation: {correlation:.2f}')

fig.write_image("correlation_plot_plotly.svg")


# Correlation Plot - Matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

plt.scatter(x, y)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Correlation Plot')

plt.savefig("correlation_plot_matplotlib.svg")



# Correlation Plot - Altair
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

data = pd.DataFrame({'Variable X': x, 'Variable Y': y})

correlation_matrix = data.corr()

alt.Chart(correlation_matrix.reset_index()).mark_rect().encode(
    x=alt.X('index:O', axis=None),
    y=alt.Y('columns:O', axis=None),
    color='value:Q'
).properties(
    width=200,
    height=200,
    title='Correlation Plot'
).save("correlation_plot_altair.svg")

