#%%

import am4894dev.netdata as nd

info = nd.api.get()

print(info['mirrored_hosts'][0])



