from django.contrib import admin
from models import PhotoGallery

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'filer_folder',)
    fields = []
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        if request.META['PATH_INFO']=='/admin/':
            return False
        else:
            return super(PhotoGalleryAdmin, self).has_change_permission(request, obj=obj)
        
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
