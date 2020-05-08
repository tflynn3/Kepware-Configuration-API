import kepware as kep
import json
client = kep.Client('dsf-piint1', 57412, use_ssl=False)

c = kep.get_channels(client, 'OPCDA01')
#post = kep.post_channels(client, '{"common.ALLTYPES_NAME":"Test","servermain.MULTIPLE_TYPES_DEVICE_DRIVER": "Simulator"}')
#print(c)

channel = kep.OPCDA(**c)

for i in range(50):
    channel.rename('OPCDA{}'.format(str(i).zfill(2)))
    result = channel.create(client)

