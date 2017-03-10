from django.contrib import admin

# page extension imports
from cms.extensions import PageExtensionAdmin

# import our model from ``models.py``
from .models import HeaderOptionsExtension
from .models import HeaderImageCopyrightExtension


class HeaderOptionsExtensionAdmin(PageExtensionAdmin):
    pass

class HeaderImageCopyrightExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(HeaderOptionsExtension, HeaderOptionsExtensionAdmin)
admin.site.register(HeaderImageCopyrightExtension, HeaderImageCopyrightExtensionAdmin)
