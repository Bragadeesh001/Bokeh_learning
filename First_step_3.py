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
