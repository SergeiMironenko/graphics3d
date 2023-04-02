import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=1,
    isomax=10,
    caps=dict(x_show=False, y_show=False)
    ))

fig.write_html('index.html')
