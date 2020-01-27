import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sys

# # wywołanie ma argumenty: 
# 1 = nazwa pliku z sygnałem, 
# 2 - cutoff na confidence

df = pd.read_csv(sys.argv[1])


# odfiltruj niskie confi
if sys.argv[2] != .6:
	cutoff = float(sys.argv[2])
else:
	cutoff = .6

df.loc[df['confidence'] < cutoff, 'diameter'] = np.nan

# zrób minima i maksima
min_obs = df.diameter.min()
max_obs = df.diameter.max()

# zrób wykres
plot_title = 'eye ' + sys.argv[2] + ' (' + sys.argv[1] + ')'
fig = px.line(df, x="time", y="diameter", color='eye_id', title= plot_title)
fig.update_layout(
    shapes=[
        # Line Vertical
        go.layout.Shape(
            type="line",
            x0=120,
            y0=min_obs,
            x1=120,
            y1=max_obs,
            line=dict(
                color="Red",
                width=2
            )
        ), 
        # Line Vertical
        go.layout.Shape(
            type="line",
            x0=240,
            y0=min_obs,
            x1=240,
            y1=max_obs,
            line=dict(
                color="Green",
                width=2
            )
        ), 
    ])
fig.write_html('plot_'+sys.argv[1]+'.html', auto_open=True)