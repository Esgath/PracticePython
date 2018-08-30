import json
import calendar
from bokeh.plotting import figure, output_file, show

def plot():
    dict_new = {}
    with open('birthjson.json', 'r') as file:
        dict = json.load(file)
    # Create new dictionary
    for k in dict:
        date = dict[k]
        if date[3] == '0':
            month = int(date[4])
        elif date[3] != '0':
            month = int(date[3:5])
        month_name = calendar.month_name[month]
        dict_new[month_name] = 0
    # Add 1 to key's value
    for k in dict:
        date = dict[k]
        if date[3] == '0':
            month = int(date[4])
        elif date[3] != '0':
            month = int(date[3:5])
        month_name = calendar.month_name[month]
        dict_new[month_name] +=1
    print(dict_new)


    output_file('plot.html')

    # X AXIS
    x_categories = [k for k in dict_new]
    # Y AXIS
    y = [dict_new[i] for i in dict_new]

    p = figure(x_range=x_categories,title="Birthday plot",
            x_axis_label='month',
            y_axis_label='number of people that have birtday',
            toolbar_location = None)
    p.vbar(x=x_categories, top=y, width=0.5)

    show(p)

plot()
