from django.contrib import admin

# page extension imports
from cms.extensions import PageExtensionAdmin

# import our model from ``models.py``
from .models import HeaderOptionsExtension

class HeaderOptionsExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(HeaderOptionsExtension, HeaderOptionsExtensionAdmin)
