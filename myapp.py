import streamlit as st

import plotly.graph_objects as go

# Create figure
fig = go.Figure()

fig.add_layout_image(
        dict(
            source="images/de_ancient.png",
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


fig.add_trace(go.Scatter(x=[100,100,200,50], y=[100,200,100,50], fill="toself"))

fig.update_layout(template="plotly_white")

fig.update_xaxes(showgrid=False, range=(0, 1024))
fig.update_yaxes(showgrid=False, scaleanchor='x', range=(1024, 0))

# fig.show()

st.plotly_chart(fig)