import pickle
import pandas as pd

# 1. PHH-ON - Connects PHH_ID to hex#, lat, lon
# 2. PHH_Speeds files - Connects internet speed metrics to PHH_ID
# 3. data com points col - city name to lat/lon
# get city - phhid (1/3), then city - speed(4/2)

# df_phh_on = pd.read_csv('data/keys/PHH-ON.csv')
# df_city_con = pd.read_csv('data/keys/Data_Com_Points_Col_Données.csv')
#
#
# # # find the closest lan/lon in ohh-on for each city in df_city_on
# # grabbing the city names we have data for
# with open('col_data.pickle', 'rb') as handle:
#     col_data = pickle.load(handle)
# city_names = []
# for name, col in col_data.items():
#     city_names.append(name)
#
# # pull only cities we have data for from df_city_con
# df_cities_info = df_city_con[df_city_con['Name_en'].str.lower().isin(city_names)].copy()
#
# # grab the lat/lon as a tuple from every item in df_cities_info
# df_cities_info['Location'] = list(zip(df_cities_info['Latitude'], df_cities_info['Longitude']))
# df_cities_loc = df_cities_info.set_index('Name_en')[['Location']]
#
# # region clean the df_cities_loc, getting rid of bad data - store in df_cities_loc
# # removing individual bad cases
# bad_cities_data = ['BURLINGTON', 'HAMILTON', 'PEMBROKE', 'STRATFORD', 'TORONTO', 'WOODSTOCK']
# df_cities_loc = df_cities_loc.drop(bad_cities_data)
#
# # specifying correct data for duplicates
# correct_locations = {
#     'Woodstock': (43.131898, -80.749269),
#     'Toronto': (43.654858, -79.383218),
#     'Stratford': (43.371537, -80.981413),
#     'Pembroke': (45.820555, -77.11111),
#     'Hamilton': (43.25757, -79.869281),
#     'Burlington': (43.37, -79.814168),
#     'Cambridge': (43.397223, -80.311389),
#     'Windsor': (42.293488, -83.051395),
#     'Kingston': (44.236342, -76.50114),
#     'Trenton': (44.110949, -77.57673),
#     'Shelburne': (44.079794, -80.202757),
#     'Milton': (43.522397, -79.870379),
#     'Georgetown': (43.646945, -79.91),
#     'Brighton': (44.040555, -77.7375),
#     'Kingsville': (42.038306, -82.738662),
#     'Caledonia': (43.069335, -79.954359),
#     'Cornwall': (45.026388, -74.726389),
#     'Vaughan': (43.852859, -79.535724),
#     'Belleville': (44.170834, -77.382778),
#     'Kincardine': (44.169444, -81.634721),
#     'Midland': (44.750277, -79.883611),
#     'Waterloo': (43.472022, -80.530122),
#     'Aylmer': (42.771978, -80.983999),
#     'Russell': (45.260304, -75.35958),
#     'Kitchener': (43.451204, -80.488043),
#     'Oakville': (43.456069, -79.690102),
#     'Leamington': (42.050834, -82.599167),
# }
#
# for cityname, loc_tuple in correct_locations.items():
#     bool_series = df_cities_loc.index == cityname
#     df_cities_loc = df_cities_loc[~(bool_series & (df_cities_loc['Location'] != loc_tuple))]
#
# duplicate_indices = df_cities_loc.index.duplicated(keep=False)
# # print(f"Duplicates Found:")
# # print(df_cities_loc[duplicate_indices])
# # endregion
#
# # region find closest tuple in df_phh_on, connect the id to city name
# # setting up ids/loc_tuple df
# df_phh_on['Location'] = list(zip(df_phh_on['Latitude'], df_phh_on['Longitude']))
# df_id_loc = df_phh_on.set_index('PHH_ID')[['Location']]
#
#
# def closest_tuple_in_list(input_tuple, list_of_tuples):
#     print(f"Input Value: {input_tuple}")
#     lowest_dif = 999999999999
#     closest_tuple = (None, None)
#     for t in list_of_tuples:
#         lat_dif = abs(input_tuple[0] - t[0])
#         lon_dif = abs(input_tuple[1] - t[1])
#         total_dif = lat_dif + lon_dif
#         if total_dif < lowest_dif:  # is a new closest value
#             closest_tuple = t
#             lowest_dif = total_dif
#     print(f"Closest Value: {closest_tuple}")
#     return closest_tuple
#
#
# city_id_dict = {}
# # finding closest tuples
# for city_name, tuple_loc in df_cities_loc.iterrows():
#     closest_tuple = closest_tuple_in_list(tuple_loc['Location'], df_id_loc['Location'])
#     phh_id = df_id_loc[df_id_loc['Location'] == closest_tuple].index[0]
#     city_id_dict[phh_id] = city_name
#
# with open('city_phhid_dict.pickle', 'wb') as handle:
#     pickle.dump(city_id_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
# # endregion
#
#
# df_speeds = pd.read_csv('data/PHH_Speeds_Current-PHH_Vitesses_Actuelles_ON.csv')
# # we want to pull "Combined_Max_Threshold-Combine_Seuil_Max". Each value will be an enum with values {"","<5_1","5_1","10_2","25_5","50_10"}
#
# # pull only rows where we have the phh_id in city_id_dict
# # with open('city_phhid_dict.pickle', 'rb') as handle:
# #     city_phhid_data = pickle.load(handle)
# phhids = []
# for phhid, cityn in city_id_dict.items():
#     phhids.append(phhid)
# df_speeds_data = df_speeds[df_speeds['PHH_ID'].isin(phhids)].copy()
#
# # create a df/dict of phh_ids and max speed value
# phhid_speeds_dict = df_speeds_data.set_index('PHH_ID')['Combined_Max_Threshold-Combine_Seuil_Max'].to_dict()
#
# with open('phhid_speeds_dict.pickle', 'wb') as handle:
#     pickle.dump(phhid_speeds_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# combining city names and speed data using phhid.
with open('city_phhid_dict.pickle', 'rb') as handle:
    phhid_city_data = pickle.load(handle)
with open('phhid_speeds_dict.pickle', 'rb') as handle:
    phhid_speeds_data = pickle.load(handle)

city_speeds_dict = {}
for phhid, city in phhid_city_data.items():
    city_speeds_dict[city] = phhid_speeds_data[phhid]

with open('city_speeds_dict.pickle', 'wb') as handle:
    pickle.dump(city_speeds_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
