import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('test')
def test_import(server):
    assert 'test' in loadedPlugins()
