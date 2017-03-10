from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool

# import our models from "models.py"
from .models import HeaderOptionsExtension
from .models import HeaderImageCopyrightExtension

@toolbar_pool.register
class HeaderOptionsExtensionToolbar(ExtensionToolbar):
    # loads the modal from "models.py"
    model = HeaderOptionsExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any)
            # and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds separator
                current_page_menu.add_break()
                # adds a toolbar item
                current_page_menu.add_modal_item(
                    'Header Options',
                    url=url,
                    disabled=not self.toolbar.edit_mode)
