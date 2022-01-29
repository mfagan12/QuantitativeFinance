import plotly.express as px
from numpy import linspace

def plot_walk(process, x_axis=None, step=1):
    num_points = len(process)
    if x_axis is None:
        x_axis = linspace(0, num_points*step, num_points)
    fig = px.line(x=x_axis, y=process)
    fig.show()