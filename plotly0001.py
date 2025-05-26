import numpy as np
import plotly.graph_objects as go

# Податоци
x = np.linspace(-3*np.pi, 3*np.pi, 500)  # Од -3π до 3π
y = np.sin(x)

# Филтрирање за да изгледа како од 3-ти квадрант кон 1-ви
x_filtered = x[x >= -3*np.pi/2]  # околу -4.7
y_filtered = y[x >= -3*np.pi/2]

# Креирање на линиска графика
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_filtered, y=y_filtered, mode='lines', name='sin(x)'))

fig.update_layout(
    title="Синусоида од 3-ти квадрант кон 1-ви квадрант",
    xaxis_title="x",
    yaxis_title="sin(x)",
    xaxis=dict(range=[-3*np.pi/2, 3*np.pi]),  # Прикажи ја оваа зона од x-оската
    yaxis=dict(range=[-1.5, 1.5])
)

fig.show()
