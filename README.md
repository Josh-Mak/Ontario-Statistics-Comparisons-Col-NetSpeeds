# Ontario-Statistics-Comparisons-Col-NetSpeeds
A simple data analysis project looking at the cost of living and internet quality across Ontarian cities.

**Intro**: I made this project to help me learn working with data using pandas. It compares internet quality/speed data from StatsCan to webscraped cost of living data, and graphs the results to see which cities have the best cost of living while still having 50/10 Mbps internet speeds. The project uses pandas, Pickle, requests, bs4, and matplotlib.

**Technical Overview**:
  1. In col_data.py, cost of living data is webscraped using requests and BeautifulSoup, and stored in a dictionary with pickle.
  2. In speeds_data.py, internet speeds and some supporting data are imported as csv files from Statistics Canada. Data is cleaned and combined to generate a dictionary with city names and according download/upload speeds.
  3. In main.py, some very simple analysis is done and the data is graphed as a scatterplot with matplotlib.

**Future Improvements**: This project more served as a way for me to learn, and a base to improve on and add more to in the future. Due to the nature of the internet speeds that I was able to obtain, the analysis was rather lackluster. Future improvements would mainly involve adding more data, such as more robust measures of internet speeds, cost of internet by city, populations, average internet downtimes, and much more.
