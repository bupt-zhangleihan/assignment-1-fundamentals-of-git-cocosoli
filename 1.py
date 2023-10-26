import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10,3)

base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
infected_dataset_url = base_url + "time_series_covid19_confirmed_global.csv"
recovered_dataset_url = base_url + "time_series_covid19_recovered_global.csv"
deaths_dataset_url = base_url + "time_series_covid19_deaths_global.csv"

infected = pd.read_csv(infected_dataset_url, index_col='Country/Region').iloc[:, 4:].sum(axis=0)
recovered = pd.read_csv(recovered_dataset_url, index_col='Country/Region').iloc[:, 4:].sum(axis=0)
deaths = pd.read_csv(deaths_dataset_url, index_col='Country/Region').iloc[:, 4:].sum(axis=0)

df = pd.DataFrame({'infected': infected,
                   'recovered': recovered,
                   'deaths': deaths})

df.index = pd.to_datetime(df.index)

df['ninfected'] = df['infected'].diff()
df['ninfected'].plot()

df['Rt'] = df['ninfected'].rolling(window=8).apply(lambda x: x[4:].sum() / x[:4].sum())
df['Rt'].plot()

plt.show()