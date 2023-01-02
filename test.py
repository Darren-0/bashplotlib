from bashplotlib.scatterplot import plot_scatter

x_coords = [-10, 0, 10]
y_coords = [-10, 0, 10]
width = 21
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
)