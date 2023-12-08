import pickle
import matplotlib.pyplot as plt

with open('col_data.pickle', 'rb') as handle:
    col_data = pickle.load(handle)
with open('city_speeds_dict.pickle', 'rb') as handle:
    city_speeds_data = pickle.load(handle)

city_col_speeds_data = {}
for city, speed in city_speeds_data.items():
    city_col_speeds_data[city] = {'col': col_data[city.lower()], 'speed': speed}

# extracting data in lists so we can plot it
cities = list(city_col_speeds_data.keys())
cols = []
speeds = []
for data in city_col_speeds_data.values():
    cols.append(data['col'])
for data in city_col_speeds_data.values():
    speeds.append(data['speed'])

lows = 0
highs = 0
for speed in speeds:
    if speed == '50_10':
        highs += 1
    else:
        lows =+ 1

print(f"Highs: {highs}")
print(f"Lows: {lows}")

# vast majority of speeds are highest value, so just graph the high value ones.
# remove the low values
city_col_data = city_col_speeds_data.copy()
items_to_remove = []
for city, values in city_col_data.items():
    if values['speed'] != '50_10':
        items_to_remove.append(city)
for city in items_to_remove:
    del city_col_data[city]

# get data in lists
cities = list(city_col_speeds_data.keys())
cols = []
for data in city_col_speeds_data.values():
    cols.append(data['col'])
cols_ints = []
for p in cols:
    s_number = p.split('%')[0]
    number = int(s_number)
    cols_ints.append(number)

plt.scatter(cities, cols_ints)
plt.show()
