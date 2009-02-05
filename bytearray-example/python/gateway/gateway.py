from pyamf.remoting.gateway.django import DjangoGateway

import python.gateway.views as views

gw = DjangoGateway({
    'ByteArray.saveSnapshot': views.save_snapshot,
    'getSnapshots': views.get_snapshots
})
