from django.conf import settings

GALLERY_IMAGE_COUNT = getattr(settings, 'CMSPLUGIN_PHOTOGALLERY_GALLERY_IMAGE_COUNT', 18)
GALLERY_PROMOTION_COUNT = getattr(settings, 'CMSPLUGIN_PHOTOGALLERY_PROMOTION_COUNT', 6)
SCROLL_TO_GALLERY = getattr(settings, 'CMSPLUGIN_PHOTOGALLERY_SCROLL_TO_GALLERY', True)
SCROLL_TO_GALLERY_DELAY = 1000  # Number of seconds to animate down to the gallery. 0 is valid too
PROMOTION_LINK_ATTR = getattr(settings, 'CMSPLUGIN_PHOTOGALLERY_PROMOTION_LINK_ATTR', 'photogallery')