def proj06_shape():
    ''
    arr_1 = two_cell_array(None, two_cell_array((3,0), two_cell_array((3,1), two_cell_array((3,2), None))))
    arr_2 = two_cell_array(arr_1, two_cell_array((2,0), two_cell_array((2,1), two_cell_array((2,2), None))))
    arr_3 = two_cell_array(arr_2, two_cell_array((1,0), two_cell_array((1,1), two_cell_array((1,2), None))))
    return_val = two_cell_array(arr_3, two_cell_array((0,0), two_cell_array((0,1), two_cell_array((0,2), None))))
    return return_val

def two_cell_array(a, b):
    return [a, b]