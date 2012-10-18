""" Views for the photogallery plugin """
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from filer.models.imagemodels import Image

try:
    import json
except:
    import simplejson as json

def ajax_get_image_info(request, image_id):
    """
        Retrieve the image that has image id sent in. and return
        info on the image
    """
    image = get_object_or_404(Image, id=image_id)
    image_info_dict = {'image_name': image.name, 'image_description': image.description,
                       'iamge_author':image.author, 'image_alt_text':image.default_alt_text,
                       'image_default_caption':image.default_caption}
    return HttpResponse(json.dumps(image_info_dict), mimetype="application/json")