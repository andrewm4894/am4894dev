#%%

from am4894dev.netdata.api import get

info = get()

print(info['mirrored_hosts'][0])



