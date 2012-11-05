""" PhotoGallery plugins """
from django.contrib.sites.models import Site
from django.template import loader

# Dependency imports
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from filer.models.imagemodels import Image

# Photo Gallery imports
from models import PhotoGallery, PhotoGalleryPromotion, HORIZONTAL, VERTICAL
from forms import PhotoGalleryPromotionPluginForm
from settings import GALLERY_IMAGE_COUNT, GALLERY_PROMOTION_COUNT, \
            SCROLL_TO_GALLERY, SCROLL_TO_GALLERY_DELAY, GALLERY_PROMOTION_COUNT,\
            PROMOTION_LINK_ATTR
            
PROMOTION_ORIENTATION_TO_TEMPLATE = {HORIZONTAL:'photogallery/photogallery_promotion_horz_plugin.html',
                                     VERTICAL:'photogallery/photogallery_promotion_vert_plugin.html'}

def get_folder_images(folder, user):
    """ Get the images from the folder. Taking into affect what iss public """
    qs_files = folder.files.instance_of(Image)
    if user.is_staff:
        return qs_files
    else:
        return qs_files.filter(is_public=True)

class PhotoGalleryPlugin(CMSPluginBase):
    """
        This class is responsible to provide the django CMS with the necessary
        information to render the PhotoGallery Plugin
    """
    module = 'Photo Gallery'
    model = PhotoGallery
    name = 'Photo Gallery'
    render_template = 'photogallery/photogallery_plugin.html'
    admin_preview = False
        
    def render(self, context, instance, placeholder):
        folder_images = get_folder_images(instance.filer_folder,
                                               context['request'].user)
        
        if len(folder_images) > GALLERY_IMAGE_COUNT:
            folder_images = folder_images[:GALLERY_IMAGE_COUNT]
                

        context.update({'gallery':instance,
                        'gallery_images':folder_images,
                        'scroll_to_gallery':SCROLL_TO_GALLERY,
                        'scroll_to_gallery_delay':SCROLL_TO_GALLERY_DELAY,
                        'promotion_link_attr':PROMOTION_LINK_ATTR})
        return context

plugin_pool.register_plugin(PhotoGalleryPlugin)

class PhotoGalleryPromotionPlugin(CMSPluginBase):
    """
        This class is responsible to provide the django CMS with the necessary
        information to render the Photo Gallery Promotion Plugin
    """
    module = 'Photo Gallery'
    model = PhotoGalleryPromotion
    name = 'Photo Gallery Promotion'
    # Note this render template is set to default but will be overrided in render
    render_template = 'photogallery/photogallery_promotion_plugin.html'
    change_form_template = 'admin/cms/page/photogallery_promotion_plugin_change_form.html'
    form = PhotoGalleryPromotionPluginForm
    admin_preview = True

    def render(self, context, instance, placeholder):
        """ Render the photo gallery promotion """
        photogallery = instance.photogallery
        folder_images = get_folder_images(photogallery.filer_folder,
                                               context['request'].user)
        
        if len(folder_images) > GALLERY_PROMOTION_COUNT:
            folder_images = folder_images[:GALLERY_PROMOTION_COUNT]
        
        # Now populate each image with a URL that can be linked to the CMS
        # page 
        prefix_url = "%s#%s%d" %(instance.page.get_absolute_url(), 
                                 PROMOTION_LINK_ATTR, photogallery.id)
        # Image indexes are 0 indexed
        index_counter = 0
        for image in folder_images:
            image.gallery_page_url = '%s-%d' %(prefix_url, index_counter)
            index_counter+=1
        
        # Template is determined by the orientation
        self.render_template = PROMOTION_ORIENTATION_TO_TEMPLATE[instance.orientation]
        context.update({'promotion':instance,
                        'gallery_images':folder_images,
                        })
        return context

plugin_pool.register_plugin(PhotoGalleryPromotionPlugin)