
# Break image into 2x2 grid (4 photos output)
# Make it scalable (future 8x8 or 16x16)
# 2hrs 

from PIL import Image


def main(img, x_grid, y_grid):
    print(img)

    i = Image.open(img)
    width, height = i.size   # Get dimensions
    print('WIDTH : {}'.format(width))
    print('HEIGHT: {}'.format(height))
    
    # grid = calc_grid(width, height, x_grid, y_grid)
    grid = calc_grid(width, height, 5, 7)
    # grid = calc_grid(800, 800, 2, 3)
    # grid = calc_grid(800, 800, 3, 3)

    for b in grid:
        cropped_example = i.crop(b)
        # cropped_example.show()


def calc_grid(width, height, x_grid, y_grid):
    # width of image
    # height of image
    # Number of x slices
    # Number of y slices
    x = 0
    y = 0
    coords = []
    for x in range(x_grid):
        for y in range(y_grid):
            c = (x,y)
            coords.append(c)
            y += 1
        x +=1
    
    print(coords)

    x_grid_size = width//x_grid
    y_grid_size = height//y_grid

    print('GRID SIZE X: {}'.format(x_grid_size))
    print('GRID SIZE Y: {}'.format(y_grid_size))

    grid = []
    for c in coords:
        x1 = c[0]*x_grid_size
        x2 = c[1]*y_grid_size
        y1 = x1 + x_grid_size
        y2 = x2 + y_grid_size

        g = (x1,x2,y1,y2)
        grid.append(g)

    # print(coords)
    print(grid)
    return grid

if __name__=='__main__':
    main('back-parking.jpg', 2,3)

    # main()

    # infile=...
    # height=...
    # width=...
    # start_num=...
    # for k,piece in enumerate(crop(infile,height,width),start_num):
    #     img=Image.new('RGB', (height,width), 255)
    #     img.paste(piece)
    #     path=os.path.join('/tmp',"IMG-%s.png" % k)
    #     img.save(path)