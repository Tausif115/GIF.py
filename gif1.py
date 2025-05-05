import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
image = []

for filename in filenames:
    image.append(iio.imread(filename))

iio.imwrite('cat.gif', image, duration = 500, loop = 0)

