from django.contrib.sites.models import Site
from django.template import loader

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import PhotoGallery, PhotoGalleryPromotion, HORIZONTAL, VERTICAL
from forms import PhotoGalleryPromotionPluginForm
from filer.models.imagemodels import Image
from settings import GALLERY_IMAGE_COUNT, GALLERY_PROMOTION_COUNT, \
            SCROLL_TO_GALLERY, SCROLL_TO_GALLERY_DELAY, GALLERY_PROMOTION_COUNT,\
            PROMOTION_LINK_ATTR

def get_folder_images(folder, user):
        qs_files = folder.files.instance_of(Image)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)

PROMOTION_ORIENTATION_TO_TEMPLATE = {HORIZONTAL:'photogallery/photogallery_promotion_horz_plugin.html',
                                     VERTICAL:'photogallery/photogallery_promotion_vert_plugin.html'}

class PhotoGalleryPlugin(CMSPluginBase):
    """
        This class is responsible to provide the django CMS with the necessary
        information to render the newsletter
    """
    module = 'Photo Gallery'
    model = PhotoGallery
    name = 'Photo Gallery'
    render_template = 'photogallery/photogallery_plugin.html'
    admin_preview = False
        
    def render(self, context, instance, placeholder):
        folder_images = get_folder_images(instance.filer_folder,
                                               context['request'].user)
        
        if len(folder_images)>GALLERY_IMAGE_COUNT:
            folder_images = folder_images[:GALLERY_IMAGE_COUNT]
        
        selected_image = None
        scroll_to_gallery = None
        gallery_key = '%s%d' % (PROMOTION_LINK_ATTR, instance.id)
        key_value =  context['request'].GET.get(gallery_key, None)
        
        if key_value:
            try:
                key_value = int(key_value)
            except ValueError:
                key_value = None
                
        if key_value and key_value and key_value < len(folder_images):
            selected_image = folder_images[key_value]
        elif folder_images:
            selected_image = folder_images[0]
        
        if key_value and SCROLL_TO_GALLERY:
            scroll_to_gallery = gallery_key
            
        context.update({'gallery':instance,
                        'gallery_images':folder_images,
                        'selected_image':selected_image,
                        'scroll_to_gallery':scroll_to_gallery,
                        'scroll_to_gallery_delay':SCROLL_TO_GALLERY_DELAY})
        return context

plugin_pool.register_plugin(PhotoGalleryPlugin)

class PhotoGalleryPromotionPlugin(CMSPluginBase):
    """
        This class is responsible to provide the django CMS with the necessary
        information to render the newsletter
    """
    module = 'Photo Gallery'
    model = PhotoGalleryPromotion
    name = 'Photo Gallery Promotion'
    render_template = 'photogallery/photogallery_promotion_plugin.html'
    change_form_template = 'admin/cms/page/photogallery_promotion_plugin_change_form.html'
    form = PhotoGalleryPromotionPluginForm
    admin_preview = False

    def render(self, context, instance, placeholder):
        
        photogallery = instance.photogallery
        folder_images = get_folder_images(photogallery.filer_folder,
                                               context['request'].user)
        
        if len(folder_images)>GALLERY_PROMOTION_COUNT:
            folder_images = folder_images[:GALLERY_PROMOTION_COUNT]
        
        gallery_page = instance.page
        
        prefix_url = "%s?%s%d" %(gallery_page.get_absolute_url(), 
                                 PROMOTION_LINK_ATTR, photogallery.id)
        index_counter = 0
        for image in folder_images:
            image.gallery_page_url = '%s=%d' %(prefix_url, index_counter)
            index_counter+=1
        
        
        self.render_template = PROMOTION_ORIENTATION_TO_TEMPLATE[instance.orientation]
        context.update({'promotion':instance,
                        'gallery_images':folder_images,
                        })
        return context

plugin_pool.register_plugin(PhotoGalleryPromotionPlugin)
