#%%

from am4894dev.netdata.api import get, get_from_info
import pprint as pp

#%%

get('allmetrics',return_type='text')
