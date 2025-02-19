from girder.api.rest import Resource
from girder.api import access
from girder.api.rest import boundHandler
from girder.api.describe import Description, autoDescribeRoute

class PublicResource(Resource):
    def __init__(self):
        super().__init__()
        self.resourceName = 'public'

        # This way we load each of the routes that we want to define within this resource
        self.route('GET', ('hello-world'), self.publicHelloWorld)
        self.route('POST', (':id', 'upload-file'), self.publicUploadFile)

    # This decorator defines access for a certain endpoint
    # access.public means that the endpoint is public
    # access.user means that the endpoint requires a user
    # access.admin means that the endpoint requires an admin
    @access.public
    # This decorator connects the function to the swagger documentation
    @autoDescribeRoute(
        Description('Get a hello world message.')
        .errorResponse())
    def publicHelloWorld(self):
        return {
            'message': 'Hello World'
        }

    @access.public
    # The following decorator makes the function behave as a method within a Resource, it is not necessary in this example
    #@boundHandler
    @autoDescribeRoute(
        Description('Upload a file with a certain id.')
        .param('id', 'The file ID', paramType='path')
        .param('upload-file', 'The file intended to be saved', required=True)
        .errorResponse())
    def publicUploadFile(self, id, params):
        self.requireParams('upload-file', params)
        return {
            'message': f'Hello, ${id}',
            'upload-file': params['upload-file']
        }

