from django.db import models

# page extension imports
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

# django filer imports
from filer.fields.image import FilerImageField

class HeaderOptionsExtension(PageExtension):
    header_subtitle = models.CharField(max_length=20, blank=True)
    header_image = FilerImageField(blank=True)

class HeaderImageCopyrightExtension(PageExtension):
    header_image_source = models.CharField(max_length=20, blank=True)
    header_image_source_url = models.CharField(max_length=255, blank=True)
    header_image_license = models.CharField(max_length=20, blank=True)
    header_image_license_url = models.CharField(max_length=255, blank=True)

extension_pool.register(HeaderOptionsExtension)
extension_pool.register(HeaderImageCopyrightExtension)
