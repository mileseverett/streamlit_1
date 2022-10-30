import streamlit as st

import plotly.graph_objects as go

from PIL import Image

img = Image.open("images/de_ancient.png")

# Create figure
fig = go.Figure()

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


# fig.add_trace(go.Scatter(x=[100,100,200,50], y=[100,200,100,50], fill="toself"))

fig.update_layout(template="plotly_white")

fig.update_xaxes(showgrid=False, range=(0, 1024), position=0)
fig.update_yaxes(showgrid=False, scaleanchor='x', range=(0, 1024))

fig.update_layout(
    autosize=False,
    width=2000,
    height=2000,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    # paper_bgcolor="LightSteelBlue",
)

# fig.show()

st.plotly_chart(fig, use_container_width=True)