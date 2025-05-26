import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Податоци - две функции, синус и косинус
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)

fig = go.Figure()

# Првата линија - синус
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))

# Втората линија - косинус
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))

# Dropdown мени за селекција на линиите
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Show sin(x)",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "sin(x)"}]),
                dict(label="Show cos(x)",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "cos(x)"}]),
                dict(label="Show Both",
                     method="update",
                     args=[{"visible": [True, True]},
                           {"title": "sin(x) and cos(x)"}]),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.15,
            yanchor="top"
        ),
    ]
)

fig.update_layout(title="Dropdown menu example with Plotly")
fig.show()
