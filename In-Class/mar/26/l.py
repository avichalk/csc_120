# Activity 1
'''
To make it easier on the user, we could make it a GUI
that is web-based so you can access it on the go.
We could draw it out graphically, following
highways and pointing out landmarks, but we could
also offer an option to print out a list of cities
for road trips and such. The tradeoffs are computational
power, and the GUI might not be able to load on an unstable
connection.
'''

# Activity 2
'''
We can have an origin point, and define the distance of each
city from it. Assuming the roads do not meander much, we can
find the distance between two towns and assume the road connecting
them is around the same length. With this implementation, we can
probably provide road names and towns and maybe a few landmarks,
but not the shape of the roads. As for time, we can store it as
an integer and convert it into human time to display.
We can store it like this:
    - HOUSTON 11.5mi
    - PHOENIX 200.3mi
    H7 HOUSTON, PHOENIX, 190.1mi
'''

# Activity 3
'''
First we load in the entire file, seperating the towns and highways into
dictionaries. Then we ask the user which two towns it would like us to find
a connection between. We find the shortest distance, find the shortest highway
connecting them, and print the information about all of this to a GUI.
'''

# WOTD: planning