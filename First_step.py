# The basic idea of Bokeh is a two-step process: First, you select from Bokeh’s building blocks to create your visualization. Second, you customize these building blocks to fit your needs.

# To do that, Bokeh combines two elements:
# A Python library for defining the content and interactive functionalities of your visualization.
# A JavaScript library called BokehJS that is working in the background to display your interactive visualizations in a web browser.




#### Creating a simple line chart ####

from bokeh.plotting import figure, show

def single_line_chart():

    #Prepare some data
    x=[1,2,3,4,5]
    y=[6,7,2,4,5]

    # create a new plot with a title and axis labels
    p = figure(title='Simple line example', x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness to the plot
    p.line(x,y, legend_label='Temp.', line_width=2)

    # show the result
    show(p)

#### Combining multiple graphs ####

def multi_line_chart():

    x=[1,2,3,4,5]
    y=[7,5,3,4,2]
    a=[4,6,8,9,5]
    b=[3,6,7,3,2]

    p = figure(title='Combined_graphs', x_axis_label='x' , y_axis_label='y' )

    p.line(x,y, legend_label='Temp.', line_width=2, color='red')
    p.line(x,a, legend_label='Rate', line_width=2, color='green')
    p.line(x,b, legend_label='Objects', line_width=2)

    show(p)