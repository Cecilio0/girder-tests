from girder import plugin
from public.public_resource import (
    PublicResource,
)

class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'test_plugin'
    CLIENT_SOURCE_PATH = 'web_client'

    def load(self, info):
        # This is the way we load an entire resource into the API
        info['apiRoot'].public = PublicResource()
        pass