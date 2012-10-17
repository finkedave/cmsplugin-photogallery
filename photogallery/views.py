from django.http import HttpResponse
from filer.models.imagemodels import Image
from django.shortcuts import get_object_or_404
try:
    import json
except:
    import simplejson as json

def ajax_get_image_info(request, image_id):
    """
        Retrieve newsletter plugin and POST the email address to the plugin's url
    """
    image = get_object_or_404(Image, id=image_id)
    
    image_info_dict = {'image_name': image.name, 'image_description': image.description}
    return HttpResponse(json.dumps(image_info_dict), mimetype="application/json")