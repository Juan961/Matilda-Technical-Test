# 🧑‍🌾 Matilda - Technical Test 


## 📕 Problem

Let’s say you hopped on a flight to the Kitzbühel ski resort in Austria. Being a software engineer you can’t help but you truly value efficiency, so naturally you start thinking it would be great to ski as long as possible and as fast as possible without having to ride back up on the ski lift. So, you take a look at the map of the mountain that a friend sent you (not very well formatted gotta say 😄) and try to find the longest ski run down.

Each number of the data matrix represents the elevation of that area of the mountain.

From each area (i.e. box) in the grid you can go north, south, east, west - but only if the elevation of the area you are going into is less than the one you are in. That means you can only ski downhill. You can start anywhere on the map; the pilot will let you choose. You are looking for a starting point with the longest possible path down as measured by the number of boxes you visit. And if there are several paths down of the same length, you want to take the one with the steepest vertical drop, which means the largest difference between your starting elevation and your ending elevation.

What a curious task, eh? Nothing a software developer would think about during a flight, right?

Your challenge is to write a program to find the longest (and then steepest) path on the given map.


### Tips
- It’s 1000x1000 in size.
- All numbers on it are between 0 and 1500.
- The path should have more than 10 steps.


## 🤓 Solution

The program starts by obtaining every possible position on the map. For each position, it looks in the directions of north, south, east, and west.

For a new position (north, south, east, or west) to be considered valid, it must meet the following conditions:

1. The direction of the new position cannot be the same as the direction I came from.
2. The position cannot be an invalid location on the map.
3. The elevation at the new position must be lower than the elevation of my current position.

If all three conditions are met, the program starts searching for the next position. The search begins from the coordinates that satisfy the conditions. When a position cannot find a valid next step, it returns the current position along with any other paths that were found in the other directions.

This process results in a complete path to a single position. Each time the program starts with a new position as the starting point in the matrix, it validates the length of the path to group the longest paths and discards the others.

After obtaining all the possible longest paths, if there is more than one, the program validates the path that has the greatest vertical distance between its starting and ending points.

## 🚀 Run

``` bash
# Mac
$ python3 main.py

# Linux
$ python3 main.py

# Windows
$ py main.py
```
