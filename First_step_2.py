# Scatter plots
# Lines and curves
# Data sources
# Ranges and axes
# Bar charts
# Area glyphs
# Grids and layouts
# Annotations

# Figure objects have many glyph methods that can be used to draw vectorized graphical glyphs:
# annular_wedge()
# annulus()
# arc()
# asterisk()
# bezier()
# circle()
# circle_cross()
# circle_dot()
# circle_x()
# circle_y()
# cross()
# dash()
# diamond()
# diamond_cross()
# diamond_dot()
# dot()
# ellipse()
# harea()
# harea_step()
# hbar()
# hex()
# hex_tile()
# image()
# image_rgba()
# image_url()
# inverted_triangle()
# line()
# multi_line()
# multi_polygons()
# oval()
# patch()
# patches()
# plus()
# quad()
# quadratic()
# ray()
# rect()
# segment()
# square()
# square_cross()
# square_dot()
# square_pin()
# square_x()
# star()
# star_dot()
# step()
# text()
# triangle()
# triangle_dot()
# triangle_pin()
# varea()
# varea_step()
# vbar()
# wedge()
# x()
# y()

from bokeh.plotting import figure, show

def Rendering_circle():

    x=[1,2,3,4,5]
    y=[7,5,3,4,2]
    a=[4,6,8,9,5]
    b=[3,6,7,3,2]

    p = figure(title='Combined_graphs', x_axis_label='x' , y_axis_label='y' )

    p.line(x,y, legend_label='Temp.', line_width=2, color='red')
    p.line(x,a, legend_label='Rate', line_width=2, color='green')
    p.circle(x,b, legend_label='Objects', size=(16))

    show(p)

def Rendering_bars():

        x=[1,2,3,4,5]
        y=[7,5,3,4,2]
        a=[4,6,8,9,5]
        b=[3,6,7,3,2]

        p = figure(title='Combined_graphs', x_axis_label='x' , y_axis_label='y' )

        p.line(x,y, legend_label='Temp.', line_width=2, color='red')
        p.vbar(x=x, top=y, legend_label='Rate', line_width=2, color='green',width = 0.5, bottom=0)
        p.circle(x,b, legend_label='Objects', size=(16))

        show(p)

def glyphs_properties():
    x=[1,2,3,4,5]
    y=[7,5,3,4,2]
    a=[4,6,8,9,5]
    b=[3,6,7,3,2]
    p = figure(title='Glyph Properties', x_axis_label='x', y_axis_label='y' )
    p.circle(x,y, legend_label='Temp.', size=16,fill_color='red', line_color='blue')
    show(p)

def altering_glyph_properties():
    x=[1,2,3,4,5]
    y=[7,5,3,4,2]
    a=[4,6,8,9,5]
    b=[3,6,7,3,2]
    p = figure(title='Glyph Properties', x_axis_label='x', y_axis_label='y' )
    circle=p.circle(x,y, legend_label='Temp.', size=16,fill_color='red', line_color='blue')

    # change color of glyph
    glyph=circle.glyph
    glyph.fill_color = 'green'
    show(p)