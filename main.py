import time


from data import get_mountain_map, get_longests_paths, get_steepest_vertical_drop_path
from utils.format import format_elevations


def main():
    try:
        start = time.time()

        mountain_map = get_mountain_map()

        longests_paths = get_longests_paths(mountain_map)

        if len( longests_paths ) == 1:
            longest_path = longests_paths[0]

            elevation = mountain_map[ longest_path[0][0] ][ longest_path[0][1] ] - mountain_map[ longest_path[-1][0] ][ longest_path[-1][1] ]

            print(f"Distance: { len( longest_path ) }. Elevation diference: { elevation }")
            print(f"Longest and steepest path in coordinates: { longests_paths[0] }")
            print(f"Path elevation view:")
            format_elevations(mountain_map, longests_paths[0])

        else:
            longest_and_steepest_path, vertical_distance = get_steepest_vertical_drop_path(mountain_map, longests_paths)
            print(f"Distance: { len(longest_and_steepest_path) }. Elevation diference: { vertical_distance }")
            print(f"Longest and steepest path in coordinates: { longest_and_steepest_path }")
            print(f"Path elevation view:")
            format_elevations(mountain_map, longest_and_steepest_path)

        end = time.time()

        # print(end - start)


    except Exception as e:
        print("An exception has ocurred")
        print(e)


if __name__ == "__main__":
    main()
