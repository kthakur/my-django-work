# Create your views here.

import glob, os.path, tempfile
from django.http import HttpResponse, get_host
from pyamf.flex import ArrayCollection

from python import gateway

def get_snapshots(http_request):
    """
    Gets a list of snapshots in the images dir

    @return: L{ArrayCollection}
    """
    l = []
    
    for jpg in glob.glob(os.path.join(gateway.images_root, '*.jpg')):
        name = jpg[len(gateway.images_root) + 1:]
        obj = {
            'url': 'http://%s/images/%s' % (get_host(http_request), name),
            'name': name
        }

        l.append(obj)

    l.reverse()

    return ArrayCollection(l[:50])

def save_snapshot(http_request, image):
    """
    Saves an image to the static image dir

    @param image: A L{pyamf.amf3.ByteArray} instance
    """
    fp = tempfile.mkstemp(dir=gateway.images_root, prefix='snapshot_', suffix='.jpg')

    fp = open(fp[1], 'wb+')
    fp.write(image.getvalue())
    fp.close()

    name = fp.name[len(gateway.images_root) + 1:]

    return {
        'url': 'http://%s/images/%s' % (get_host(http_request), name),
        'name': name
    }

