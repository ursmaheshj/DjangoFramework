# Function Based Middleware
def funcMiddleware(get_response):
    print('--------one-time configuration/initialization---------')
    def myMiddleware(request):
        print('-----Code execute before view-------')
        response = get_response(request)
        print('-----Code execute After view-------')
        return response
    return myMiddleware
