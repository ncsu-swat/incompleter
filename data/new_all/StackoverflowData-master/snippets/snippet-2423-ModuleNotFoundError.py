#Source: https://stackoverflow.com/questions/62275064/python-tuples-typeerror-bool-object-is-not-subscriptable
import math, random
import numpy as np
import skimage.io as io

# Please do not alter this function.
def show_image(data, routes=[]):
    '''
    Given a list of lists of integers "data",
    and an optional list of boolean list of lists "routes",
    show the data as an image and overlay the routes on the image in red.
    '''
    image_data = [x[:] for x in data]
    for i in range(len(image_data)):
        for j in range(len(image_data[i])):
            image_data[i][j] = [image_data[i][j]] * 3
            if any(route[i][j] for route in routes):
                image_data[i][j] = [255, 0, 0]
    io.imshow(np.array(image_data, dtype=np.uint8))
    io.show()

def load_dat_file(filename):

    data = []
    data = np.loadtxt(filename)

    data_temp = []
    try: 
        for item in data:
            item = str(item).replace('.', '').replace('[', '').replace(']', '').split()
            data_temp.append(item)
        data = data_temp
    except:
        print("error")

    return data

def find_elevation_route_for_starting_row(grid, starting_row):

    boolean_list = []
    elevation_change = 0

    for index_grid in range(len(grid)):
        boolean_route = []
        for index_grid_item in range(len(grid[index_grid])):
            boolean_grid_item = False
            if (index_grid == starting_row):
                boolean_grid_item = True
                if (index_grid_item + 1 < len(grid[index_grid])):
                    absolute_value = abs(int(grid[index_grid][index_grid_item + 1]) - int(grid[index_grid][index_grid_item]))
                    elevation_change = elevation_change + absolute_value
            boolean_route.append(boolean_grid_item)
        boolean_list.append(boolean_route)

    return (boolean_list, elevation_change)

def get_all_elevation_routes(grid):

    boolean_list_grid = []
    elevation_change_grid = []

    for index_grid in range(len(grid)):
        current_elevation_route = find_elevation_route_for_starting_row(grid, index_grid)
        boolean_list_grid.append(current_elevation_route[0])
        elevation_change_grid.append(current_elevation_route[1])


    return tuple(boolean_list_grid), tuple(elevation_change_grid)

def get_min_elevation_route(routes):

    routes_boolean_list = routes[0]
    routes_elevation_change_list = routes[1]
    lowest_route_index = 0

    for index_routes_elevation_change_list in range(len(routes_elevation_change_list)):
        if (routes_elevation_change_list[index_routes_elevation_change_list] < routes_elevation_change_list[lowest_route_index]):
            lowest_route_index = index_routes_elevation_change_list


    return tuple(routes_boolean_list[lowest_route_index]) 

# Please do not alter anything below this line.
if __name__ == '__main__':
    data = load_dat_file("mountroyal.dat")
    show_image(data, [])
    routes = get_all_elevation_routes(data)

    min_route = get_min_elevation_route(routes)
    assert(isinstance(min_route, tuple))

    show_image(data, [min_route[0]])
    show_image(data, [route for route, change in routes])