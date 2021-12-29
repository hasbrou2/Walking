import pygal
from die import Die

#Create a D6.
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
#Make some rolls, and store results in a list.
results=[]
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist._title = "Results of rolling one D6 D6 D6 50,000 times."
hist.x_labels = []
for x in range(3, 19):
    hist.x_labels.append(x)

hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6' + 'D6' + 'D6', frequencies)
hist.render_to_file('die_visual.svg')