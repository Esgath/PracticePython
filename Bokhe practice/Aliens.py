import random
from bokeh.plotting import figure, output_file, show


colors = ['green', 'red', 'black', 'yellow', 'purple']
fleet = {}
for i in range(1,31):
    fleet["alien_" + str(i)] = {}
    fleet["alien_" + str(i)]["colors"] = random.choice(colors)

color_count = {}
for i in range(1,31):
    color = fleet["alien_" + str(i)]["colors"]
    if color in color_count:
        color_count[color] += 1
    elif fleet["alien_" + str(i)]["colors"] not in color_count:
        color_count[color] = 0

output_file("aliens.html")
x_categories =[k for k in color_count]
y =[v for v in color_count.values()]

p = figure(x_range=x_categories)
p.vbar(x=x_categories, top = y, width = 0.5)
show(p)
