#%%

from am4894dev.netdata.api import get, get_from_info
import pprint as pp

#%%

info = get('info')

print(info['mirrored_hosts'][0])

#%%

pp.pprint(info)
#get_from_info(info,'collectors')
