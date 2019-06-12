#!/usr/bin/python
'''
Sikorsky Interview Question
Date:   June 11, 2019
Author: Joseph Samela

$ python main.py back-parking.jpg 5 3
> `back-parking.jpg` is path to the image
> `5` number of grid divisions, x-axis
> `3` number of grid divisions, y-axis
'''
import sys
from PIL import Image


def main(path, x_grid, y_grid):
    # Open image, get dimensions
    img = Image.open(path)
    width, height = img.size

    # Calculate grid
    grid = calc_grid(width, height, x_grid, y_grid)

    # Score tiles
    scores = []
    for tile in grid:
        score = score_tile_redness(img, tile)
        scores.append((tile, score))

    # Sort tiles by score
    # More RED (high score) --> Less RED (low score)
    sorted_scores = sorted(scores, key=lambda tup: tup[1], reverse=True)

    # Save tiles to ./tiles
    for idx, tile in enumerate(sorted_scores):
        coord = tile[0]
        score = tile[1]
        t = img.crop(coord)
        t.save('./tiles/{}.{}.{}.jpg'.format(idx,coord,score))


def calc_grid(width, height, x_grid, y_grid):
    '''Calculate list of coordinates describing each tile

    Args:
        width  (int): width of image in px
        height (int): height of image in px
        x_grid (int): number of slices, x-axis
        y_grid (int): number of slices, y-axis

    Returns:
        tiles (list): List of tuples describing coordinates of each tile
    '''

    # Calculate grid dimensions
    x_grid_size = width//x_grid
    y_grid_size = height//y_grid
    # Notice `//` the decimal component is thrown away

    '''
    The grid is comprised of tiles.
    Each tile is described by two coordinates...
    "a" is the upper-left
    "b" is the bottom-right

    a  _______
      |       |
      |  tile |
      |       |
       ------- b

    tile_coordinates = (a1, a2, b1 ,b2)
    '''
    a = 0
    b = 0
    coords = []
    for a in range(x_grid):
        for b in range(y_grid):
            c = (a,b)
            coords.append(c)
            b += 1
        a +=1

    '''
    The coordinates generated assume a grid of 1 dimension.
    the distances need to be scaled by the grid dimensions
    ditermined by the image size in pixels.
    '''
    grid = []
    for c in coords:
        a1 = c[0]*x_grid_size
        a2 = c[1]*y_grid_size
        b1 = a1 + x_grid_size
        b2 = a2 + y_grid_size
        g = (a1,a2,b1,b2)
        grid.append(g)

    return grid


def score_tile_redness(img, tile):
    '''Read image pixel-by-pixel to score the amount of red present

    Args:
        img  (obj): PIL.Image() reference to open image
        tile (tup): tile coordinates as tuple (a1,a2,b1,b2)

    Returns:
        score (int): Score (+ or -) indicating the amount of red in the photo
    '''
    tile = img.crop(tile)
    colors = tile.getdata()
    score = 0
    for c in colors:
        score = score + c[0] - c[1] - c[2]
        '''
        c is the RGB color of each pixel as a tuple (R,G,B)
        the "redness" of each pixel is calculated as:

        redness = RED - GREEN - BLUE

        For example, take this candy-apple red color: (227,46,86)
        redness = 227-46-86 = 95
        '''
    return score


if __name__=='__main__':

    # Parse arguments
    if len(sys.argv) != 3:
        print('')
    image_path = sys.argv[1]
    x_grid_div = int(sys.argv[2])
    y_grid_div = int(sys.argv[3])

    main(image_path, x_grid_div, y_grid_div)
