### Adding legend text and annotations ###

from bokeh.plotting import figure, show

def modify_legend():
    x=[1,2,3,4,5]
    y=[6,7,5,3,2]
    y1=[3,5,7,3,1]

    p = figure(title='Modifying Legend')
    p.line(x,y, legend_label='Temp.', line_color='black', line_width=2)
    circle=p.circle(x,y1, legend_label='circle.', fill_color='black')
    glyph=circle.glyph
    glyph.fill_color='green'

    p.legend.location='top_left'
    p.legend.title='Observations'
    p.legend.click_policy='hide'

    # change appearance of legend text
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"

    # change border and background of legend
    p.legend.border_line_width = 3
    p.legend.border_line_color = "navy"
    p.legend.border_line_alpha = 0.8
    p.legend.background_fill_color = "navy"
    p.legend.background_fill_alpha = 0.2
    
    show(p)
    


### Customising Headlines ###

def customize_headlines():
    x=[1,2,3,4,5]
    y=[6,7,5,3,2]

    p=figure(title="Customisation Headlines")
    p.vbar(x=x,top=y, legend_label='Bar', color='black', width=0.5, bottom=0)

    # Change the headline location to left
    p.title_location = "left"

    # Change headline text
    p.title.text = "Modified Headlines"

    # Style the headlines
    p.title.align = "center"
    p.title.text_font = "times"
    p.title.text_font_style = "italic"
    p.title.text_color = "navy"
    p.title.text_font_size = "25pt"
    p.title.background_fill_color='black'
    show(p)

### Annotations ###
## https://docs.bokeh.org/en/latest/docs/user_guide/basic/annotations.html#ug-basic-annotations ##

def annotations():
    from bokeh.models import BoxAnnotation

    low_box = BoxAnnotation(top=3, fill_alpha=0.2, fill_color='black')
    mid_box = BoxAnnotation(bottom=3, top=5.5, fill_alpha=0.2, fill_color='red')
    high_box = BoxAnnotation(bottom=5.5, fill_alpha=0.2, fill_color='green')

    x=[1,2,3,4,5]
    y=[6,7,5,3,2]

    p=figure(title="Annotations")
    p.line(x,y, legend_label='annotation', line_color='navy', 
           line_width=2)
    
    p.add_layout(low_box)
    p.add_layout(mid_box)
    p.add_layout(high_box)

    show(p)
