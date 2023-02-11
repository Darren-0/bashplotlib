from bashplotlib.scatterplot import plot_scatter
from bashplotlib.histogram import plot_hist

'''height = 20
bincount = 5
binwidth = 20'''

plot_hist(
    'hist_data.txt',
    title = "test histogram",
    showSummary=True
)

'''x_coords = [-10, 20, 30]
y_coords = [-10, 20, 30]
width = 10
char = 'x'
color = 'red'
title = 'My Test Graph'
xs_title = "The X axis"
ys_title = "The Y axis"

plot_scatter(
    None, 
    x_coords, 
    y_coords, 
    width, 
    char, 
    color, 
    title, 
    xs_title, 
    ys_title
)'''
