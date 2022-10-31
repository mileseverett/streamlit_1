import streamlit as st

import plotly.graph_objects as go

import plotly.graph_objects as go

from PIL import Image

img = Image.open("images/de_ancient.png")

# Create figure
fig = go.Figure()

# # Add trace
# fig.add_trace(
#     go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1], )
# )

fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=0,
            y=0,
            sizex=1024,
            sizey=1024,
            # sizing="stretch",
            opacity=1,
            layer="below")
)

# fig.add_shape(
#     type=, xref='x', yref='y',
#     x0=650, x1=1080, y0=380, y1=180, line_color='cyan'
# )

fig.add_trace(go.Scatter(x=[100,100,200,50], y=[100,200,100,50], fill="toself"))

fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="PaleTurquoise",
    x0=35, y0=35, x1=45, y1=45,
    line_color="LightSeaGreen"
)

# Set templates
fig.update_layout(template="plotly_white")

fig.update_xaxes(showgrid=False, range=(0, 1024),visible=False, fixedrange=True)
fig.update_yaxes(showgrid=False, scaleanchor='x', range=(1024, 0),visible=False, fixedrange=True)

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    paper_bgcolor="LightSteelBlue",
)

config = {"displayModeBar":False}


# fig.show()

st.plotly_chart(fig, config=config)