from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

file = pd.read_excel('Book1.xlsx')
file.to_csv('Book1.csv')
print(file.head())

df = pd.read_csv('Book1.csv')

# create new figure, axes instances.
fig=plt.figure(figsize=(8,8))
ax=fig.add_axes([0.1,0.1,0.8,0.8])

# setup mercator map projection.
m = Basemap(llcrnrlon=43.,llcrnrlat=23.,urcrnrlon=65.,urcrnrlat=41.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)


m.drawcoastlines()
m.fillcontinents()
m.drawcountries()

lon = df["lon"]
lat = df["lat"]
population = df["population"]
colors = ['red','blue','green','purple','black','white','pink','yellow','brown','grey']

x, y = m(lon, lat)

m.scatter(x, y, s=population*60,color=colors)

legend_elements = [Patch(facecolor=colors[i], label=df['city'][i]) for i in range(len(df))]
plt.legend(handles=legend_elements, loc='upper right')

ax.set_title('Iran')
plt.show()