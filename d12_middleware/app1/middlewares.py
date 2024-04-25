from django.shortcuts import HttpResponse


# Function Based Middleware
def funcMiddleware(get_response):
    print('--------func:one-time configuration/initialization---------')
    def myMiddleware(request):
        print('-----func:Code execute before view-------')
        response = get_response(request)
        # response = HttpResponse('Cant go forward, response from middleware')
        print('-----func:Code execute After view-------')
        return response
    return myMiddleware

# Class Based Middleware
class classMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('--------class:one-time configuration/initialization---------')
    def __call__(self,request):
        print('-----class:Code execute before view-------')
        response = self.get_response(request)
        # response = HttpResponse('Cant go forward, response from middleware')
        print('-----class:Code execute After view-------')
        return response
    def process_view(self,request,*args, **kwargs):
        print('----------class:Inside processview-run before view--------')

class middlewareHook:
    def __init__(self,get_response):
        self.get_response = get_response
        print('--------hooks:one-time configuration/initialization---------')
    def __call__(self,request):
        print('-----hooks:Code execute before view-------')
        response = self.get_response(request)
        print('-----hooks:Code execute After view-------')
        return response
    def process_view(self,*args, **kwargs):
        print('----------hooks:Inside processview-run before view--------')
    def process_exception(self,request,exception):
        print('------hooks:process_exception(Exception occured)------')
        msg = exception
        className = exception.__class__.__name__
        return HttpResponse(f'from process_exception:{className}:{msg}')
    def process_template_response(self,request,response):
        print('---------hooks:Process template response----------')
        response.context_data['name']='Mahadev'
        return response