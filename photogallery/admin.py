from django.contrib import admin
from models import PhotoGallery, PhotoGalleryPromotion


class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'filer_folder',)
    
class PhotoGalleryPromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'photogallery', 'orientation')
    raw_id_fields = ('photogallery', 'page')
    radio_fields = {"orientation": admin.HORIZONTAL}
    
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoGalleryPromotion, PhotoGalleryPromotionAdmin)
