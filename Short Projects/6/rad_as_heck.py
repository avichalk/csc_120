import graphics

def main():
    '''
    Handles most of our inputs and all sorts of extraneous stuff,
    though I do like the colours.
    '''
    print("Let's create a Forest of Triangles!")
    x = input('How many iterations would you like? (Note: >7 it becomes difficult to see new triangles, and is very taxing on the system)\n')
    color = input('Would you like some colour in your triangles? Y/N/INVERT!\n')
    gui = graphics.graphics(1000, 1000, "Sierpinski Triangle")
    while not gui.is_destroyed():
        gui.clear()
        array = [[125, 125, 875, 125, 500, 875]] # theoretically, to change the size of the triangle, you only have to change this array
        #array = [[10, 10, 990, 10, 500, 990]]
        #contents: [x1, y1,  x2,  y2,  x3, y3] in a list inside another list. That is important for later.
        if color == 'Y':
            colours = ['white', 'pink', 'light blue', 'green', 'red', 'yellow', 'blue']
            gui.triangle(array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5], fill = 'purple')
            gui.text(10, 950, "It's Christmas!")
        elif color == 'N':
            gui.text(10, 950, "This is a Sierpinski Triangle! As our iterations approach infinity it will end up having 0 area but an infinite perimeter!", size=9)
            gui.triangle(array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5])
            colours = ['white', 'white', 'white', 'white', 'white', 'white', 'white']
        elif color == 'INVERT!':
            gui.rectangle(0, 0, 1000, 1000)
            gui.text(10, 950, "You got it!", fill='white')
            gui.triangle(array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5], fill='white')
            colours = ['black', 'black', 'black', 'black', 'black', 'black', 'black']
        else:
            gui.triangle(array[0][0], array[0][1], array[0][2], array[0][3], array[0][4], array[0][5])
            colours = ['white', 'pink', 'light blue', 'green', 'red', 'yellow', 'blue']
            gui.text(10, 950, "If you're undecided, here's both!")
        create_sierpinski(gui, array, int(x), colours)

def create_sierpinski(gui, array, x, colours):
    '''
    A Sierpinski Triangle is a fractal where one triangle is
    divided into three smaller triangles by removing a triangle
    in the centre. This is not what we are doing, however- instead,
    we are adding one white triangle in the centre of every black
    triangle (or diff. if you selected the color option). In essense,
    each triangle has three halfway points, each of which spawn three new
    triangles. Each element in array contains one triangle's coordinates,
    and we divide their sides in half and create new triangles. We then take
    the coordinates of the three new triangles and pass them into the function again.
    This is recursive and incredibly taxing, but it's very pretty.
    '''
    z = 0
    if x != 0:
        arr = []
        for i in array:
            ar = [(i[0]+i[2])/2, (i[1]+i[3])/2, (i[0]+i[4])/2, (i[1]+i[5])/2, (i[2]+i[4])/2, (i[5]+i[3])/2] # halfway points
            gui.triangle((i[0]+i[2])/2, (i[1]+i[3])/2, (i[0]+i[4])/2, (i[1]+i[5])/2, (i[2]+i[4])/2, (i[5]+i[3])/2, fill=colours[z]) # print triangle
            gui.update_frame(100) # update is here so we get that cool maze effect. By moving it to the end of the for loop, we get one update per x iteration.
            arr.append([i[0], i[1], ar[0], ar[1], ar[2], ar[3]]) # child one
            arr.append([i[2], i[3], ar[0], ar[1], ar[4], ar[5]]) # child two
            arr.append([i[4], i[5], ar[2], ar[3], ar[4], ar[5]]) # child three
            if z == 6:
                z = 0 # this handles our finite color list. Kinda wish we had access to the full rgb suite...
            z += 1
        create_sierpinski(gui, arr, x-1, colours)

main()