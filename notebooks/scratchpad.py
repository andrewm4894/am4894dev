#%%

from am4894dev.netdata.api import get_chart_data

df = get_chart_data('system.io')
print(df.shape)
print(df.head())

