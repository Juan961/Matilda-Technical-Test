def get_mountain_map():
    mountain_map = []

    with open('./data/map.txt', 'r') as file:
        rows, columns = file.readline().split(" ") # Dimentions

        lines = file.readlines()

        for line in lines:
            mountain_map.append( list( map( lambda item: float(item), line.split(" ") ) ) )

        file.close()

    return mountain_map


def get_longests_paths(mountain_map):
    paths = [ [] ]

    for row_index in range( len( mountain_map ) ):
        for column_index in range( len( mountain_map[row_index] ) ):
            path = get_longest_path_starting_point(mountain_map, row_index, column_index)

            if len( path ) > len( paths[0] ):
                paths.clear()

            elif len( path ) < len( paths[0] ):
                continue

            paths.append(path)

    return paths


def get_longest_path_starting_point(mountain_map, row, column, from_direction = None):
    try:
        path = [ [ row, column ] ]

        CURRENT_HEIGHT = mountain_map[ row ][ column ]

        HEIGHT_EAST = mountain_map[ row ][ column + 1 ]
        HEIGHT_SOUTH = mountain_map[ row + 1 ][ column ]
        HEIGHT_WEST = mountain_map[ row ][ column - 1 ]
        HEIGHT_NORTH = mountain_map[ row - 1 ][ column ]

        new_path_east = []
        new_path_south = []
        new_path_west = []
        new_path_north = []

        # Search east
        if from_direction != "east" and column + 1 <= len(mountain_map[row]) and CURRENT_HEIGHT > HEIGHT_EAST:
            new_path_east = get_longest_path_starting_point(mountain_map, row, column + 1, "east")

        # Search south
        if from_direction != "south" and row + 1 <= len(mountain_map) and CURRENT_HEIGHT > HEIGHT_SOUTH:
            new_path_south = get_longest_path_starting_point(mountain_map, row + 1, column, "south")

        # Search west
        if from_direction != "west" and column - 1 >= 0 and CURRENT_HEIGHT > HEIGHT_WEST:
            new_path_west = get_longest_path_starting_point(mountain_map, row, column - 1, "west")

        # Search north
        if from_direction != "north" and row - 1 >= 0 and CURRENT_HEIGHT > HEIGHT_NORTH:
            new_path_north = get_longest_path_starting_point(mountain_map, row - 1, column, "north")


        if len(new_path_east) > len(new_path_south) and len(new_path_east) > len(new_path_west) and len(new_path_east) > len(new_path_north):
            path.extend(new_path_east)


        elif len(new_path_south) > len(new_path_east) and len(new_path_south) > len(new_path_west) and len(new_path_south) > len(new_path_north):
            path.extend(new_path_south)


        elif len(new_path_west) > len(new_path_south) and len(new_path_west) > len(new_path_east) and len(new_path_west) > len(new_path_north):
            path.extend(new_path_west)


        elif len(new_path_north) > len(new_path_south) and len(new_path_north) > len(new_path_west) and len(new_path_north) > len(new_path_east):
            path.extend(new_path_north)


        return path


    except IndexError as e:
        return [ [ row, column ] ]


def get_steepest_vertical_drop_path(mountain_map, longests_paths):
    distance = 0
    longest_and_steepest_path = []

    for longests_path in longests_paths:
        start_path = longests_path[0]
        end_path = longests_path[-1]

        path_steepest_vertical_distance = mountain_map[ start_path[0] ][ start_path[1] ] - mountain_map[ end_path[0] ][ end_path[1] ]
        
        if path_steepest_vertical_distance > distance:
            distance = path_steepest_vertical_distance
            longest_and_steepest_path = longests_path

    return longest_and_steepest_path, distance
