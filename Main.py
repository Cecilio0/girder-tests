
def uploadFile(file_path, file_name = 'file.txt', mime_type = None, collection_name = 'test-collection', folder_name = 'test-folder', item_name = 'test-item', parent_id = None, parent_type = None):

    if parent_id and parent_type:
        return gc.uploadFile(parent_id, file_path, file_name, 'text/plain', parent_type, mimeType=mime_type)

    # Create 'test-collection' collection if it does not exist
    collection = None

    for col in gc.listCollection():
        if col['name'] == collection_name:
            collection = col

    if not collection:
        collection = gc.createCollection(collection_name, 'A collection created to test the girder client', False)

    # Create a folder 'test-folder' within the collection
    folder = None

    for fol in gc.listFolder(collection['_id'], 'collection'):
        if fol['name'] == folder_name:
            folder = fol

    if not folder:
        folder = gc.createFolder(collection['_id'], folder_name, 'A folder created to test the girder client','collection')

    # Create an item 'test-item' within the folder
    item = None

    for listedItem in gc.listItem(folder['_id']):
        if listedItem['name'] == item_name:
            item = listedItem

    if not item:
        item = gc.createItem(folder['_id'], item_name, 'An item created to test the girder client', 'collection')

    # Create a file 'test-file' within the item
    return gc.uploadFileToItem(item['_id'], file_path, '', mime_type, file_name)

if __name__ == "__main__":
    from girder_client import GirderClient
    gc = GirderClient(apiUrl='http://127.0.0.1:8080/api/v1')

    girder_token = gc.authenticate('cecilio', 'password')
    # girder_token = gc.authenticate(interactive=True)
    # girder_token = gc.authenticate(apiKey='3Dyjb0Boqlcu9QvzGjjqs9eeLpoiPDDAV3uYlPdC')
    # girder_token = gc.authenticate(apiKey='5GzN5cnSHaKT8naxNdvek5UfQ4AaWosSYaMAw2iPgOO1rDes8CTirFlQNEW8Autd')

    # It is important to consider that folders, items and files can also be created under a user or under their default public and private folders
    # It is also important to consider trying out Groups for user access to certain collections, folders, items or files
    # uploadFile('./test-file.txt')


    # A very similar method to this one can be called to download an entire item
    file_id = '67bbb7ffb571ef3331accf8b'
    gc.downloadFile(file_id, './downloads/download.txt')

    # resource_id = '67bbb7ffb571ef3331accf88' # folder
    resource_id = '67bb8ff08889106c3c7cbbc2' # user
    # dest = './downloads/new-folder'
    dest = './downloads/new-user'
    # resource_type = 'folder'
    resource_type = 'user'
    gc.downloadResource(resource_id, dest, resource_type)


