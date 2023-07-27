### Customizing your plot ###

### Using Themes ###    

# With Bokeh’s themes, you can quickly change the appearance of your plot. Themes are a set of pre-defined design parameters such as colors, fonts, or line styles.
# Bokeh comes with five built-in themes: caliber, dark_minimal, light_minimal, night_sky, and contrast. Additionally, you can define your own custom themes.

def themes():
    from bokeh.io import curdoc
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]
    # y1=[8,4,3,6,9]

    curdoc().theme = 'dark_minimal'

    p = figure(max_width=500, height=400, title="Themes")
    p.line(x,y)

    # curdoc().theme = 'caliber'
    # f= figure(title='Diff theme')
    # f.line(x,y1)

    show(p)
    # show(f)


    ### Setting width and height ###

def width_height():
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]


    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x', 
        y_axis_label='y')
    
    p.line(x,y)

    show(p)

def resizing():
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]


    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x', 
        y_axis_label='y')
    
    p.width = 300
    p.height = 800
    
    p.line(x,y)

    show(p)

def responsive_sizing():
    from bokeh.plotting import figure, show 

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]

    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x',
        sizing_mode='stretch_width') #Adjusts the plot automatically based on webpage #
    
    p.line(x,y)

    show(p)

### Setting your axes appearance ###

def axes():
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]

    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x',
        y_axis_label='y')
    
    # Change some things about the x-axis
    p.xaxis.axis_label = 'Temp'
    p.xaxis.axis_label_text_font_size = '12pt'
    p.xaxis.axis_line_color='red'

    # Change some things about the y-axis
    p.yaxis.axis_label = 'Pressure'
    p.yaxis.axis_label_text_font_size = '12pt'
    p.yaxis.axis_line_color='navy'
    p.yaxis.axis_label_orientation='vertical'

    # Change things on all axes
    p.axis.minor_tick_in=-30
    p.axis.minor_tick_out=66
    
    p.line(x,y)
    show(p)


### Defining axes range ###

def axes_range():
    from bokeh.plotting import figure, show

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]
    
    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x',
        y_axis_label='y',
        y_range=(0,25),
        x_range=(0,50))
    
    p.line(x,y)
    show(p)

### Formatting axis ticks ###
def axis_ticks():
    from bokeh.plotting import figure, show
    from bokeh.models import NumeralTickFormatter

    x=[1,2,3,4,5]
    y=[6,4,3,1,3]
    
    p = figure(
        width=500, 
        height=400, 
        title="width and height",
        x_axis_label='x',
        y_axis_label='y',
        y_range=(0,25),
        x_range=(0,50))
    
    if p.yaxis:
        p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
    else:
        print('not working')
    
    p.line(x,y)
    show(p)
    

def background_color():
    from bokeh.plotting import figure, show

    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [4, 5, 5, 7, 2]

    # create a plot
    p = figure(
        title="Background colors example",
        sizing_mode="stretch_width",
        max_width=500,
        height=250,
    )

    # add a renderer
    p.line(x, y, line_color="green", line_width=2)

    # change the fill colors
    p.background_fill_color = (204, 255, 255)
    p.border_fill_color = (102, 204, 255)
    p.outline_line_color = (0, 0, 255)

    # show the results
    show(p)

### Positioning the toolbar
# p.figure(title="Toolbar position", toolbar_position='below')

### Deactivating toolbar
# p.toolbar_location = None

### Toolbar logo none
# p.toolbar.loge = None





