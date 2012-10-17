from django.conf.urls.defaults import *

urlpatterns = patterns('photogallery.views',
    (r'^photogallery/ajax/get_image_info/(?P<image_id>\d+)/', 'ajax_get_image_info'),
)
