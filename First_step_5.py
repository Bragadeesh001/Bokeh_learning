### Vectorizing glyph ###`

## Vectorizing graph

def vectorizing_gluph():
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]


    p = figure(
        width=500, 
        height=400, 
        title="vectorized color samples",
        x_axis_label='x', 
        y_axis_label='y')
    
    line=p.line(x,y,line_color = 'navy',line_width = 1)
    circle=p.circle(x,y,fill_color = 'red',line_width = 1, size = 10)

    show(p)