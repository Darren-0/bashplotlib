from bashplotlib.scatterplot import _plot_scatter

x_coords = [-10, 0, 10]
y_coords = [-10, 0, 10]
width = 10
char = 'x'
color = 'red'
title = 'My Test Graph'
xs_title = "The X axis"
ys_title = "The Y axis"

test_a = _plot_scatter( 
    x_coords, 
    y_coords, 
    width, 
    char, 
    color, 
    title,
    None, 
    xs_title, 
    ys_title
)
expected_result_a = '''+------------------------+
|+----------------------+|
||    My Test Graph     ||
|+----------------------+|
+------------------------+
y: The Y axis
--------------------------
|           |         x  |
|           |            |
|           |            |
|           |            |
|           |            |
| - - - - - x - - - - -  |
|           |            |
|           |            |
|           |            |
|           |            |
| x         |            |
--------------------------
             x: The X axis'''

test_b = _plot_scatter( 
    [-10, 3, 5, 10], 
    [-10, 0, 0, 10], 
    width, 
    char, 
    color, 
    title, 
    None, 
    xs_title, 
    ys_title
)

expected_result_b = '''+------------------------+
|+----------------------+|
||    My Test Graph     ||
|+----------------------+|
+------------------------+
y: The Y axis
--------------------------
|           |         x  |
|           |            |
|           |            |
|           |            |
|           |            |
| - - - - - o - x x - -  |
|           |            |
|           |            |
|           |            |
|           |            |
| x         |            |
--------------------------
             x: The X axis'''

test_c = _plot_scatter( 
    [-10, 3, 3, 10], 
    [-10, 0, 0, 10], 
    width, 
    char, 
    color, 
    title, 
    None, 
    xs_title, 
    ys_title
)

expected_result_c = '''+------------------------+
|+----------------------+|
||    My Test Graph     ||
|+----------------------+|
+------------------------+
y: The Y axis
--------------------------
|           |         x  |
|           |            |
|           |            |
|           |            |
|           |            |
| - - - - - o - x - - -  |
|           |            |
|           |            |
|           |            |
|           |            |
| x         |            |
--------------------------
             x: The X axis'''

if test_a == expected_result_a:
    print('SUCCESS')
else:
    print('FAILURE')
if test_b == expected_result_b:
    print('SUCCESS')
else:
    print('FAILURE')
if test_c == expected_result_c:
    print('SUCCESS')
else:
    print('FAILURE')