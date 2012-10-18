from models import PhotoGalleryPromotion
from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib.admin.sites import site

class PhotoGalleryPromotionPluginForm(forms.ModelForm):
    """ Custom form to make the Plugin display the fields correctly """
    class Meta:
        model = PhotoGalleryPromotion
        widgets = {
            'orientation': forms.RadioSelect,
            'photogallery': ForeignKeyRawIdWidget(PhotoGalleryPromotion._meta.get_field(
                                        'photogallery').rel, site),
            'page': ForeignKeyRawIdWidget(PhotoGalleryPromotion._meta.get_field(
                                        'page').rel, site),
        }