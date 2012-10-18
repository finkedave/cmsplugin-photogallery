from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page  
from filer.fields.folder import FilerFolderField

class PhotoGallery(CMSPlugin):
    title = models.CharField(null=False, blank=False, max_length=80,
                        help_text=_('Enter the Photo Gallery title.'))
    filer_folder = FilerFolderField()
    
    def __unicode__(self):
        return 'Photo gallery %s' % self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Photo galleries'
        
VERTICAL = 'v'
HORIZONTAL = 'h'
ORIENTATION_CHOICES = ((HORIZONTAL, 'Horizontal'),
                       (VERTICAL, 'Vertical'))
class PhotoGalleryPromotion(CMSPlugin):
    photogallery = models.ForeignKey(PhotoGallery, null=False, blank=False)
    page = models.ForeignKey(Page, null=False, blank=False,
                             help_text=_('Select a page that contains the gallery.'))
    title = models.CharField(null=False, blank=False, max_length=80,
                        help_text=_('Enter the Photo Gallery title.'))
    description = models.CharField(null=False, blank=False, max_length=255,
                        help_text=_('Enter the Photo Gallery description.'))
    orientation = models.CharField(null=False, blank=False, max_length=1, choices=ORIENTATION_CHOICES,
                                   help_text=_('The orientation that the the images will be displayed in'),
                                   default=HORIZONTAL)
    
    def __unicode__(self):
        return 'Photo gallery promotion %s' % self.title
    
    class Meta:
        ordering = ['title']