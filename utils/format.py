def format_elevations(mountain_map, path):
    for i in range( len( path ) ):
        print(" " * i + f"{ mountain_map[ path[i][0] ][ path[i][1] ] }")
