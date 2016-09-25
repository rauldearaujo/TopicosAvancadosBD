import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot(data):
	coord = data[:,2:4]
	fig = plt.figure()


	themap = Basemap(projection='gall',
              llcrnrlon = -40,              # lower-left corner longitude
              llcrnrlat = -6,               # lower-left corner latitude
              urcrnrlon = -35,               # upper-right corner longitude
              urcrnrlat = -3,               # upper-right corner latitude
              resolution = 'l',
              area_thresh = 100000.0,
              )
              
	themap.drawcoastlines()
	themap.drawcountries()
	themap.fillcontinents(color = 'gainsboro')
	themap.drawmapboundary(fill_color='steelblue')

	x, y = themap(coord[:,0], coord[:,1])
	themap.plot(x, y, 
	            'o',                    # marker shape
	            color='Indigo',         # marker colour
	            markersize=4            # marker size
	            )

	plt.show()
